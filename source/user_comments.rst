User Comments
=============

User Comments 페이지는 연구신 인원들이 Indy API를 사용하면서 겪었던 문제점과 해결 방법을 공유하는 공간입니다. 이 페이지는 연구신 인원들이 Indy API를 보다 효율적으로 사용할 수 있도록 돕기 위해 만들어졌습니다.

API의 경우 버전이 계속 수정되니 반드시 현재 펌웨어 버전에 맞는 명령어를 사용하기 바란다.

Official Document
-----------------
- `DCP3 : gRPC(google Remote Procedure Call) 기반의 통신 프로토콜<http://docs.neuromeka.com/3.4.0/kr/IndyAPI/indydcp3_1/>`
- `DCP2 : TCP/IP 기반의 통신 프로토콜<http://docs.neuromeka.com/3.4.0/kr/IndyAPI/indydcp2_1/>`
- `ROS : Robot Operating System<http://docs.neuromeka.com/3.4.0/kr/ROS/introduction/#_2>`
- `ROS2 : Robot Operating System 2<http://docs.neuromeka.com/3.4.0/kr/ROS2/introduction/>`

Indy API
-----------------
현재는 gRPC인 Indy DCP3가 공식적으로 배포되고 있으며, 사용하고 있다. 연구실에서는 주로 Python을 사용하여 명령을 주고 있으며, 모든 명령어는 공식 문서에 명시되어 있다.

설치 방법
-------

터미널이나 명령 프롬프트에서 다음 명령어를 사용하여 패키지를 설치할 수 있습니다.

.. code-block:: bash

   pip3 install neuromeka

아래 터미널 명령을 통해 패키지 버전 업데이트가 가능합니다.

.. code-block:: bash

   pip3 install --upgrade neuromeka

현재 설치된 패키지의 버전은 아래 터미널 명령을 통해 확인할 수 있습니다.

.. code-block:: bash

   pip3 show neuromeka


IndyDCP3 사용방법
---------------

클라이언트 객체를 생성하기 위해서는 ``neuromeka`` 패키지에서 ``IndyDCP3`` 클래스를 임포트해야 합니다.

.. code-block:: python

   from neuromeka import IndyDCP3

IndyDCP3 클래스 객체를 생성한 후, 로봇과 통신을 위해 다음과 같이 로봇의 IP 주소를 지정합니다.

.. code-block:: python

   indy = IndyDCP3(robot_ip='192.168.0.10', index=0)

- ``robot_ip`` : 로봇 컨트롤러 IP 주소
- ``index`` : 양팔 로봇처럼 로봇 컨트롤러에 여러 대의 로봇이 연결된 경우 로봇 인덱스


사용방법 및 함수
-------------

아래부터는 ``IndyDCP3`` 객체를 이용하여 호출 가능한 프로토콜 함수들의 리스트입니다.
각 함수의 사용방법과 입출력 예제를 참고하여 사용할 수 있습니다.

.. note::
   모든 함수의 출력은 Python ``dict`` 타입으로 반환됩니다.

실시간 데이터 획득 함수
------------------

로봇의 현재 모션 상태, 제어 데이터 및 상태, 서보 모터의 상태, 에러 사항, 그리고 프로그램 상태 등을 반환받을 수 있습니다.

.. list-table::
   :header-rows: 1
   :widths: 35 65

   * - Function
     - Description
   * - ``get_control_state()``
     - 제어 상태
   * - ``get_motion_data()``
     - 모션 데이터
   * - ``get_servo_data()``
     - 서보 데이터
   * - ``get_ft_sensor_data()``
     - 힘/토크 센서 데이터
   * - ``stop_motion(stop_category)``
     - stop_category에 따라 모션을 멈추는 함수
     - stop_category : CAT0(power off), CAT1(stop & power off), CAT2(stop)
   * - ``movej(input)``
     - 관절 위치 제어 명령
     - input : 관절 위치 리스트 (단위: degree)
     - input(option) : vel_ratio, acc_ratio, jtarget, base_type
   * - ``movel(input)``
     - 작업공간에서의 선형 위치 제어 명령
     - input : 작업공간 위치 리스트 (단위: mm, degree)
     - input(option) : vel_ratio, acc_ratio, teaching_mode, base_type
   * - ``recover()``
     - 에러나 충돌 상황에서 로봇을 회복시키는 함수
