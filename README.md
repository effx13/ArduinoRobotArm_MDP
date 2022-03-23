# 인천전자마이스터고등학교 2학년 MDP 프로젝트
얼굴 인식 모니터암 작품 소스코드

### 기능
- 사용자의 얼굴을 자동으로 추적하여 사용자가 가장 편안한 위치로 이동합니다.
- 안드로이드 앱을 이용하여 수동으로 위치를 조정할 수 있습니다.
- 1분 이상 사용하지 않으면 자동으로 설정된 위치로 돌아갑니다.

### 사용 기술
- [OpenCV](https://opencv.org/)
- [ArduinoJson](https://arduinojson.org/)

### 설치
##### 라즈베리파이
    sudo apt-get install python3 pip
    pip install opencv-python bluetooth
    git clone https://github.com/effx13/ArduinoRobotArm_MDP.git
    cd ArduinoRobotArm_MDP/RaspberryPi/
    python3 main.py
#### 아두이노
    git clone https://github.com/effx13/ArduinoRobotArm_MDP.git
    cd ArduinoRobotArm_MDP/Arduino/main/
이후 ArduinoJson 설치 후 빌드 및 업로드

#### 안드로이드
    git clone https://github.com/effx13/ArduinoRobotArm_MDP.git
    cd ArduinoRobotArm_MDP/Android/
이후 Android Studio를 이용하여 앱 빌드
    
    
