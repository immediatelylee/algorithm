    /**
     * checkout용(네이버페이, 카카오페이) : 특정기기에서 ajax 비동기화시 이슈가 되어 동기화로 호출 By ECHOSTING-512334
     * is_prd 업데이트
     *
     * @param array aParam post전송할 파라미터
     * @param object 클릭한 element 객체
     */
     _checkoutcallOrderAjax : function(aParam) {
        EC$.ajax({
            type: 'POST',
            url: '/exec/front/order/order/',
            async: false,
            data: aParam,
            dataType: 'json',
            success: function(data) {
                if (data.result < 0) {
                    alert(data.alertMSG);
                    return;
                }
            }
        });
    },

    /**
     * 선택한 상품금액 계산하기
     * @param array aParam post전송할 파라미터
     */
    _callCalcAjax : function(aParam) {

        if (bCheckedProductCalc === true) {
            BasketAppDiscount.doCalculate(aParam, sDiscountApp);
        }
    },

    /**
     * '△' 버튼 클릭, 수량증가
     * @param sId: 변경시킬 폼 id
     * @param int iIdx 품목정보 배열 인덱스
     */
    addQuantityShortcut: function(sId, iIdx)
    {
        //var iQuantity = parseInt(EC$('#'+sId).val(), 10) + this.getBuyUnit(iIdx);
        var iQuantity = aBasketProductData[iIdx].quantity + this.getBuyUnit(iIdx);
        if (isNaN(iQuantity) === false) {
            EC$('#'+sId).val(iQuantity);
        }
        this.modifyQuantity(sId);
    },
    /**
     * '▽' 버튼 클릭, 수량감소
     * @param sId : 클릭한 id
     * @param int iIdx 품목정보 배열 인덱스
     */
    outQuantityShortcut: function(sId, iIdx)
    {
        //var iQuantity = parseInt(EC$('#'+sId).val(), 10) - this.getBuyUnit(iIdx);
        var iQuantity = aBasketProductData[iIdx].quantity - this.getBuyUnit(iIdx);
        if (iQuantity < 1) iQuantity = 1;
        if (isNaN(iQuantity) === false) {
            EC$('#'+sId).val(iQuantity);
        }
        this.modifyQuantity(sId);
    },

    /**
     * 구매 주문단위값 가져오기
     * @param int iIdx 품목정보 배열 인덱스
     */
    getBuyUnit: function(iIdx)
    {
        try {
            if (bIsNewProduct) {
                return aBasketProductData[iIdx].buy_unit;
            }
        } catch (e) {}

        return 1;
    },

    /**
     * 장바구니 리스트의 '주문하기' 버튼 클릭
     * @param iIdx: 품목정보 배열 인덱스
     */
    orderBasketItem: function(iIdx)
    {
        // 각 항목별 수량체크에 성공할 경우에 주문페이지로 이동.
        if (this.isAbleQuantityForMaxMinSingle(iIdx)) {
            var aData = [];
            var iProdNo = aBasketProductData[iIdx].product_no;
            var sOptId = aBasketProductData[iIdx].opt_id;
            var sProductType = aBasketProductData[iIdx].product_type;
            var sIsSetProduct = aBasketProductData[iIdx].is_set_product;
            var iBasketPrdNo = aBasketProductData[iIdx].basket_prd_no;
            var iCustomDataIdx = aBasketProductData[iIdx].custom_data_idx;
            var sDelvType = aBasketProductData[iIdx].delvtype;

            // 장바구니 분리형세트 상품 판단을 위한 세트번호
            var iSetPrdNo = parseInt(aBasketProductData[iIdx].set_product_no);

            // 분리형세트의 선택주문시 관련세트 구성 전부 체크후 선택주문하기처리
            if (iSetPrdNo > 0) {
                this.setAddSingleSetItemCheckedAction(iSetPrdNo, 'orderSelectBasket');
                return false;
            }

            var sKey = iProdNo + ':' + sOptId + ':' + sIsSetProduct + ':' + iBasketPrdNo + ':' + iCustomDataIdx + ':' + sDelvType;

            aData.push(sKey);

            this._callOrderAjax({
                checked_product: aData.join(','),
                basket_type: this._getBasketType(sProductType),
                delvtype: sBasketDelvType
            });
        }
    },

    /**
     * 장바구니상 분리형세트 단독 처리 불가능하게 액션처리
     */
    setAddSingleSetItemCheckedAction: function(iSetPrdNo, sAction)
    {

        for (i = 0; i < aBasketProductData.length; i++) {
            if (aBasketProductData[i].set_product_no == iSetPrdNo) {
                EC$("#" + BASKET_CHK_ID_PREFIX + i).prop("checked", true);
            } else {
                EC$("#" + BASKET_CHK_ID_PREFIX + i).prop("checked", false);
            }
        }

        // 선택액션 임시 엘리먼트 생성
        var oTmpElem = document.createElement('a');
        oTmpElem.id = 'oBasketSetAction';
        oTmpElem.setAttribute("link-login","/member/login.html");
        oTmpElem.setAttribute("link-order","/order/orderform.html?basket_type=all_buy");

        switch (sAction) {
            case 'orderSelectBasket' : this.orderSelectBasket(oTmpElem); break;
            case 'deleteBasket' : this.deleteBasket(); break;
           // case 'orderSelectBasket' : this.orderSelectBasket(); break;

        }

    },

    /**
     * 장바구니 리스트의 '관심상품등록' 버튼 클릭
     * @param iIdx: 품목정보 배열 인덱스
     */
    addWishListItem: function(iIdx)
    {
        var aData = [];
        var iProdNo = aBasketProductData[iIdx].product_no;
        var sOptId = aBasketProductData[iIdx].opt_id;
        var sProductType = aBasketProductData[iIdx].product_type;
        var sIsSetProduct = aBasketProductData[iIdx].is_set_product;
        var iBasketPrdNo = aBasketProductData[iIdx].basket_prd_no;
        var sKey = iProdNo + ':' + sOptId + ':' + sIsSetProduct + ':' + iBasketPrdNo;
        aData.push(sKey);
        this._callBasketAjax({
            command: 'select_storage',
            checked_product: aData.join(','),
            delvtype: sBasketDelvType
        });
    },
    /**
     * 장바구니 리스트의 '삭제' 버튼 클릭
     * @param iIdx: 품목정보 배열 인덱스
     */
    deleteBasketItem: function(iIdx)
    {
        // 장바구니 분리형세트 상품 판단을 위한 세트번호
        var iSetPrdNo = parseInt(aBasketProductData[iIdx].set_product_no);

        // 분리형세트의 선택주문시 관련세트 구성 전부 체크후 선택주문하기처리
        if (iSetPrdNo > 0) {
            this.setAddSingleSetItemCheckedAction(iSetPrdNo, 'deleteBasket');
            return false;

        }

        if (confirm(__('선택하신 상품을 삭제하시겠습니까?')) == false) return;

        if (typeof ACEWrap !== 'undefined') {
            ACEWrap.delCheckedBasket();
        }
        var aData = [];
        var iProdNo = aBasketProductData[iIdx].product_no;
        var sOptId = aBasketProductData[iIdx].opt_id;
        var sProductType = aBasketProductData[iIdx].product_type;
        var sIsSetProduct = aBasketProductData[iIdx].is_set_product;
        var iBasketPrdNo = aBasketProductData[iIdx].basket_prd_no;
        var iCustomDataIdx = aBasketProductData[iIdx].custom_data_idx;
        var sDelvType = aBasketProductData[iIdx].delvtype;

        var sKey = iProdNo + ':' + sOptId + ':' + sIsSetProduct + ':' + iBasketPrdNo + ':' + iCustomDataIdx + ':' + sDelvType;

        aData.push(sKey);
        this._callBasketAjax({
            command: 'select_delete',
            checked_product: aData.join(','),
            delvtype: sBasketDelvType
        });
    },
    /**
     * 장바구니 리스트의 체크박스 전체선택
     * @param sBoxName: 선택할 종류이름
     * @param oElem: object 클릭한 element 객체
     */
    setCheckBasketList: function(sBoxName, oElem)
    {
        if (this._existsBasket(true) == false) return;
        EC$('input[name="'+ sBoxName +'"]:checkbox').each(function() {
            if (EC$(oElem).prop('checked') === true) {
                EC$(this).prop('checked', true);
            } else {
                EC$(this).prop('checked', false);
            }
        });

        // 전체 선택 여부
        sAllChecked = 'F';
        if (EC$('[id^="basket_chk_id_"]:checked').length == EC$('[id^="basket_chk_id_"]').length || EC$('[id^="basket_chk_id_"]:checked').length == 0) { //전체선택 or 전체해제
            sAllChecked = 'T';
        }
        
        Basket._callCalcAjax({
            checked_product: Basket._getCheckedProductList().join(','),
            all_checked : sAllChecked
        });
    },

    /**
     * 각각의 장바구니 아이템별로 객체화한다.
     * @param iIndex 장바구니인덱스.
     * @return Object 장바구니내의 개별 아이템객체
     */
    makeBasketPrdInfo: function(iIndex) {
        var iProdNo = aBasketProductData[iIndex].product_no;
        var sOptId = aBasketProductData[iIndex].opt_id;
        var sKeyProdWithOpt = iProdNo + '__' + sOptId;

        var objBasketPrdInfo = [];

      if (objBasketPrdInfo.length == 0) {
      // [상품번호__옵션]별 객체 초기화.
          objBasketPrdInfo[sKeyProdWithOpt] = {
                "minMaxKey": sKeyProdWithOpt,
                "buyUnitKey": sKeyProdWithOpt,
                "quantity": 0,
                "min": 0,
                "max": 0,
                "maxType": "F",
                "buy_unit": 1,
                "product_name_quantity": aBasketProductData[iIndex].product_name.replace(/\\(.)/mg, "$1"),
                "product_name_buy_unit": aBasketProductData[iIndex].product_name.replace(/\\(.)/mg, "$1")
            };
        }

//      폼전송이 발생하기전 화면에 입력된 값은 무시. (2015-12-11)
//      objBasketPrdInfo[sKeyProdWithOpt].quantity += parseInt(EC$('#quantity_id_'+ iIndex).val());
        objBasketPrdInfo[sKeyProdWithOpt].quantity = aBasketProductData[iIndex].quantity;
        // ECHOSTING-336171 대응
        // 1+N 상품 일 경우, 주문수량 제한 > 최대 주문수량 체크 하지 않음
        objBasketPrdInfo[sKeyProdWithOpt].maxType = aBasketProductData[iIndex].sIsBenefitEventProduct == 'T' ? 'F' : aBasketProductData[iIndex].product_max_type;
        //objBasketPrdInfo[sKeyProdWithOpt].maxType  = aBasketProductData[iIndex].product_max_type;
        objBasketPrdInfo[sKeyProdWithOpt].min = aBasketProductData[iIndex].product_min;
        objBasketPrdInfo[sKeyProdWithOpt].max = aBasketProductData[iIndex].product_max;
        objBasketPrdInfo[sKeyProdWithOpt].buy_unit = aBasketProductData[iIndex].check_buy_unit;

        if (Olnk.isLinkageType(aBasketProductData[iIndex].option_type) === true) {
            objBasketPrdInfo[sKeyProdWithOpt].min = aBasketProductData[iIndex].product_min;
            objBasketPrdInfo[sKeyProdWithOpt].max = aBasketProductData[iIndex].product_max;
        }

        if (aBasketProductData[iIndex].check_quantity_type == 'P') {
            objBasketPrdInfo[sKeyProdWithOpt].minMaxKey = iProdNo;
        } else {
            objBasketPrdInfo[sKeyProdWithOpt].product_name_quantity += aBasketProductData[iIndex].opt_str.replace(/\\(.)/mg, "$1");
        }

        if (aBasketProductData[iIndex].check_buy_unit_type == 'P') {
            objBasketPrdInfo[sKeyProdWithOpt].buyUnitKey = iProdNo;
        } else {
            objBasketPrdInfo[sKeyProdWithOpt].product_name_buy_unit += aBasketProductData[iIndex].opt_str.replace(/\\(.)/mg, "$1");
        }

        return objBasketPrdInfo[sKeyProdWithOpt];
    },


    /**
     * 최소/최대 주문가능 수량 체크
     * @param boolean bIsAll 전체상품주문여부
     * @return boolean
     */
    isAbleQuantityForMaxMin: function(bIsAll)
    {
        var aBasketPrdInfo = [];
        var aBasketCheckQuantity = [];
        var aBasketCheckBuyUniyQuantity = [];
        for (var i=0,n=aBasketProductData.length; i < n; i++) {
            // 선택상품 주문인경우 선택한 상품에 대해서만
            if (bIsAll == false) {
                if (EC$("#" + BASKET_CHK_ID_PREFIX + i).prop("checked") === false) {
                    continue;
                }
            }

            if (aBasketProductData[i].check_quantity_type == 'P') {
                var sKey = aBasketProductData[i].product_no;
                if (typeof aBasketCheckQuantity[sKey] === 'undefined') {
                    aBasketCheckQuantity[sKey] = aBasketProductData[i].quantity;
                } else {
                    aBasketCheckQuantity[sKey] += aBasketProductData[i].quantity;
                }
            } else {
                var sKey = aBasketProductData[i].product_no + '__' + aBasketProductData[i].opt_id;
                aBasketCheckQuantity[sKey] = aBasketProductData[i].quantity;
            }

            if (aBasketProductData[i].check_buy_unit_type == 'P') {
                var sKey = aBasketProductData[i].product_no;
                if (typeof aBasketCheckBuyUniyQuantity[sKey] === 'undefined') {
                    aBasketCheckBuyUniyQuantity[sKey] = aBasketProductData[i].quantity;
                } else {
                    aBasketCheckBuyUniyQuantity[sKey] += aBasketProductData[i].quantity;
                }
            } else {
                var sKey = aBasketProductData[i].product_no + '__' + aBasketProductData[i].opt_id;
                aBasketCheckBuyUniyQuantity[sKey] = aBasketProductData[i].quantity;
            }

            aBasketPrdInfo.push(this.makeBasketPrdInfo(i));
        }

//        alert(aBasketPrdInfo.toString());
        // 유효성 체크
        var iBasketPrdCnt = aBasketPrdInfo.length;
        for (var index = 0; index < iBasketPrdCnt; index++) {
            // 최소구매수량 체크
            var iProductMinCount = aBasketPrdInfo[index].min <= 0 ? 1 : aBasketPrdInfo[index].min;
            if (aBasketCheckQuantity[aBasketPrdInfo[index].minMaxKey] < iProductMinCount) {
                alert(aBasketPrdInfo[index].product_name_quantity+' '+sprintf(__('최소 주문수량은 %s개 입니다.'), iProductMinCount));
                this.resetQuantityFromBasket();
                return false;
            }
            // 최대구매수량 체크
            if ((aBasketPrdInfo[index].maxType == 'T' && aBasketPrdInfo[index].max > 0)
                    && aBasketPrdInfo[index].max < aBasketCheckQuantity[aBasketPrdInfo[index].minMaxKey]) {
                alert(aBasketPrdInfo[index].product_name_quantity+' '+sprintf(__('최대 주문수량은 %s개 입니다.'), aBasketPrdInfo[index].max));
                this.resetQuantityFromBasket();
                return false;
            }

            if ((aBasketCheckBuyUniyQuantity[aBasketPrdInfo[index].buyUnitKey] % aBasketPrdInfo[index].buy_unit) > 0) {
                alert(aBasketPrdInfo[index].product_name_buy_unit+' '+sprintf(__('구매 주문단위는 %s개 입니다.'), aBasketPrdInfo[index].buy_unit));
                return false;
            }
        }

        return true;
    },

    /**
     * 최소/최대 주문가능 수량 체크 (단일상품)
     * @param boolean iIndex 장바구니 인덱스.
     * @return boolean
     */
    isAbleQuantityForMaxMinSingle: function(iIndex)
    {
        var aBasketPrdInfo = [];
        aBasketPrdInfo.push(this.makeBasketPrdInfo(iIndex));
        // 유효성 체크
        // 최소구매수량 체크
        var iProductMinCount = aBasketPrdInfo[0].min <= 0 ? 1 : aBasketPrdInfo[0].min; //구상품 최소 구매수량 0으로 저장 가능
        if (aBasketPrdInfo[0].quantity < iProductMinCount) {
            alert(sprintf(__('최소 주문수량은 %s개 입니다.'), iProductMinCount));
            this.resetQuantityFromBasket();
            return false;
        }
        // 최대구매수량 체크
        if ((aBasketPrdInfo[0].maxType == 'T' && aBasketPrdInfo[0].max > 0)
                && aBasketPrdInfo[0].max < aBasketPrdInfo[0].quantity) {
            alert(sprintf(__('최대 주문수량은 %s개 입니다.'), aBasketPrdInfo[0].max));
            this.resetQuantityFromBasket();
            return false;
        }

        if ((aBasketPrdInfo[0].quantity % aBasketPrdInfo[0].buy_unit) > 0) {
            alert(sprintf(__('구매 주문단위는 %s개 입니다.'), aBasketPrdInfo[0].buy_unit));
            return false;
        }

        return true;
    },

    /**
     * 상품수량 장바구니 정보로 초기화
     */
    resetQuantityFromBasket: function()
    {
        try {
            for (var i=0,n=aBasketProductData.length; i < n; i++) {
                var iOldQty = parseInt(aBasketProductData[i].quantity);
                var iCurQty = parseInt(EC$('#quantity_id_'+i).val());
                if (iOldQty != iCurQty) {
                    EC$('#quantity_id_'+i).val(iOldQty);
                }
            }
        } catch (e) {}
    },

    /**
     * 옵션변경 레이어 노출
     * @param string sId 옵션변경 layer id
     */
    showOptionChangeLayer: function(sId, oThis)
    {
        var aIndex = sId.split("_");
        var iIndex = aIndex[3];
        var iSetIndex = sId.split("_")[4];

        if (EC$("#ec-basketOptionModifyLayer").length > 0) { // 비동기 옵션 변경 레이어 사용일경우 - ECHOSTING-229719
            /** 추가/변경 버튼 클릭 이벤트 끊어주기 **/
            EC$(".ec-basketOptionModifyLayer-add").off("click");
            EC$(".ec-basketOptionModifyLayer-modify").off("click");
            /** 선택옵션, 추가옵션 템플릿 제외하고 다 지워주기 **/
            EC$("#ec-basketOptionModifyLayer").find(".ec-basketOptionModifyLayer-options").slice(1).remove();
            EC$("#ec-basketOptionModifyLayer").find(".ec-basketOptionModifyLayer-addOptions").slice(1).remove();
            
            var aParam = {
                iIndex: iIndex,
                iSetIndex: iSetIndex,
                aProductData: aBasketProductData[iIndex]
            };

           EC$.ajax({
                type: 'POST',
                url: '/exec/front/Product/OptionForm/',
                data: aParam,
                dataType: 'json',
                async: false,
                success: function(data) {
                  if (data.result == 0) {
                    var aProductOption = data.aProductOption; 
                    EC$(".ec-basketOptionModifyLayer-productName").html(aProductOption.product_name);
                    EC$(".ec-basketOptionModifyLayer-optionStr").html(aProductOption.layer_option_str);
 
                    /** 선택 옵션 **/
                    for (let i = 0; i < aProductOption.optionList.length; i++) {
                        var oOptionElement = EC$(".ec-basketOptionModifyLayer-options").first().clone();
                        var sOptionElement = oOptionElement.html();
                        sOptionElement = sOptionElement.replace(/{\$option_name}/g, aProductOption.optionList[i].option_name);
                        sOptionElement = sOptionElement.replace(/{\$form.option_value}/g, aProductOption.optionList[i].form_option_value);
                        oOptionElement.html(sOptionElement);
                        EC$(".ec-basketOptionModifyLayer-options").last().after(oOptionElement.show());
                    }

                    /** 추가입력 옵션 **/
                    for (let i = 0; i < aProductOption.optionAddList.length; i++) {
                        var oOptionElement = EC$(".ec-basketOptionModifyLayer-addOptions").first().clone();
                        var sOptionElement = oOptionElement.html();
                        sOptionElement = sOptionElement.replace(/{\$option_name}/g, aProductOption.optionAddList[i].option_name);
                        sOptionElement = sOptionElement.replace(/{\$form.option_value}/g, aProductOption.optionAddList[i].form_option_value);
                        oOptionElement.html(sOptionElement);
                        EC$(".ec-basketOptionModifyLayer-addOptions").last().after(oOptionElement.show());
                    }
                    
                    /** 옵션 추가 버튼 **/
                    if (aProductOption.option_add_display == true) {
                        EC$(".ec-basketOptionModifyLayer-add").show();
                        EC$(".ec-basketOptionModifyLayer-add").click(function() {
                            BasketNew.modify(iIndex, 'add');
                        });
                    } else {
                        EC$(".ec-basketOptionModifyLayer-add").hide();
                    }

                    /** 옵션 변경 버튼 **/
                    EC$(".ec-basketOptionModifyLayer-modify").click(function() {
                        if (aBasketProductData[iIndex]['is_set_product']=='T' && aBasketProductData[iIndex]['set_product_no']==0) {
                            NewBasketSetOption.modify(iIndex, iSetIndex); // 일체세트
                        } else {
                            BasketNew.modify(iIndex, 'modify');
                        }
                    });

                    /** 옵션 폼 이벤트 초기화 **/
                    CAFE24.SHOP_FRONT_NEW_OPTION_COMMON.initObject();
                    CAFE24.SHOP_FRONT_NEW_OPTION_COMMON.init();
                    CAFE24.SHOP_FRONT_NEW_OPTION_BIND.initChooseBox();
                    CAFE24.SHOP_FRONT_NEW_OPTION_DATA.initData();
                  }
                }
            });

            /** 옵션변경 이벤트 발생시킨 엘리먼트 바로 뒤에 붙여줌 **/
            oThis.after(EC$("#ec-basketOptionModifyLayer"));
            EC$("#ec-basketOptionModifyLayer").show();
            
        } else {
            EC$("[id^='option_modify_layer']").hide();
            EC$(".optionModify").hide();
            EC$("#" + sId).show();

            if (bIsNewProduct === true) {
                EC$("#" + sId).find('[id^="product_option_id"]').eq(0).val('*').trigger('change');
            }
        }
    },
    /**
     *  상품명위에 [당일배송][퀵배송] 문구 노출
     *  @param aPrdNo : 장바구니페이지의 상품번호 array
     */
    isCustomshipAjax: function(aQuickPrdNo, aQuickItemCode)
    {
        if (!aQuickItemCode) return;
        var aParam = {};
        var sDeliveryAreaAjaxUrl = '/exec/front/order/Basketcustomship/';

        aParam['aPrdNo'] = aQuickPrdNo;
        aParam['aItemCode'] = aQuickItemCode;

        EC$.ajax({
            type: 'POST',
            url: sDeliveryAreaAjaxUrl,
            data: aParam,
            dataType: 'json',
            async: false,
            success: function(data) {
                if (data.result == 0) {
                    var sToday = data.sDisplayToday;
                    var sQuick = data.sDisplayQuick;

                    try {
                        for (var key1 in sQuick) {
                            if (sQuick[key1] == 'T') EC$('[id^="custom_quick_id_show_' + key1 + '"]').removeClass('displaynone');
                            if (sQuick[key1] == 'T') EC$('[id^="custom_quick_id_' + key1 + '"]').html(sQuick['sc_name']);
                        }
                        for (var key in sToday) {
                            if (sToday[key] == 'T') EC$('[id^="custom_today_id_show_' + key + '"]').removeClass('displaynone');
                            if (sToday[key] == 'T') EC$('[id^="custom_today_id_' + key + '"]').html(sToday['sc_name']);
                        }
                    } catch (e) {}
                }
            }
        });
    },
