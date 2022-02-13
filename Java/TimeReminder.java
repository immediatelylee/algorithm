// 129p checkpoint
import java.util.Calendar;

public interface TimeProvider {//인터페이스 도입
    public void setHours(int hours);
    public int getTime();
}

public class FakeTimeProvider implements TimeProvider {
    //TimeProvider 테스트 스탭
    private Calendar cal;
    public FakeTimeProvider(){
        cal = Calendar.getInstance();
    }

    public FakeTimeProvider(int hours){
        cal = Calendar.getInstance();
        setHours(hours);
    }

    public void setHours(int hours){
        cal.set(Calendar.HOUR_OF_DAY,hours); // 주어진 시간으로 시간 설정
    }
    public int getTime(){
        return cal.get(Calendar.HOUR_OF_DAY);// 현재시간 반환
    }
}

public class TimeReminder {
    TimeProvider tProv;
    m = new MP3();
    public void setTimeProvider(TimeProvider tProv){
        this.tProv = tProv.getTime();
        if (hours >= 22) {
            m.playSong();
        }
    }    
}
