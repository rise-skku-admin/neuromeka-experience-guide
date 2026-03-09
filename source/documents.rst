Documents
=========

Official Document
-----------------

- `Neuromeka Docs <http://docs.neuromeka.com/>`_


ROS Manual
----------------
- `Indy ros <https://github.com/neuromeka-robotics/indy-ros>`_
- `Indy ros examples <https://github.com/neuromeka-robotics/indy-ros-examples>`_


**SDK3 Deployment**


⚠️ **주의 사항: 반드시 실행중인 제어기를 끄고 실행할 것**



- 제어기 죽이기
    
    ```bash
    sudo pkill -09 UDEVMonitor
    sudo pkill -09 python3
    sudo pkill -09 ProcessManager
    ps -ef |grep Task # 여기 나오는 process ID를 확인하여 종료
    sudo kill -09 <process_id> 
    ```
    
- 커스텀 제어기 실행
    
    ```bash
    cd ~/release/IndyDeployment
    python3 indy_run.py
    ```
    

STEP3 : 64bit VScode에서 SSH접속 가능

STEP2 : 32bit VScode에서 SSH접속 불가능(vim, nano, vi 등을 이용해 터미널 편집 필요)

