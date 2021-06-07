<h3  align="center">시각장애인을 위한 횡단보도 통행 보조 시스템 </h3>

  

<p  align="center">

보행자 신호등에서 시각장애인들은 보조장치인 음향신호기를 통해 도움을 받을 수 있지만 종종 불편한 위치에 설치되어 있어 불편함을 겪는다. 본 프로젝트에서는 이러한 문제와 한계점을 개선하고자 Computer Vision 기반의 object detection 모델을 이용한 개선방안을 제시한다.

<br  />
<br  />
<br  />
<!-- TABLE OF CONTENTS -->

<details  open="open">

<summary><h2  style="display: inline-block">Content</h2></summary>

<ol>

<li>

<a href="#about-the-project">프로젝트에 대해서</a>
</li>
<li>
<a  href="#EDA">EDA</a>
</li>
<li>
<a  href="#performance">성능</a>
</li>
<li>
<a  href="#conclusion">정리</a>
</li>
</ol>
</details>

<!-- ABOUT THE PROJECT -->

## About The Project
시각장애인들이 홀로 도보를 이용하는 것은 상당한 위험이 따른다. 이러한 시각장애인들을 위해 점자블록, 음향신호기 등 보조장치들이 마련되어 있지만 시각장애인을 고려하지 않은 설치로 인해 실질적인 사용에 어려움이 있다 . 특히 시각장애인들은 보행신호등에서 가장 많은 위험을 느낀다는 설문조사 결과도 있다. 이처럼 교통약자인 시각장애인을 보조하는 장치하는 이미 존재하지만 실질적으로 시각장애인에게 도움을 주지 못하고 있는 상황이다. 그래서 이를 해결하고자 실제 신호등에 부착되어 사용할 수 있도록 소형 컴퓨텅에서 시각 장애인을 감지하는 시스템을 만든 프로젝트이다.

 
<!-- EDA -->

## EDA
[![EDA1][데이터 분포1]](https://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/EDA1.jpg?raw=true){: width="100" height="100"}

[![EDA2][데이터 분포2]](https://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/EDA2.jpg?raw=true){: width="100" height="100"}

### 이미지 예시
현재 수집하고 가공한 이미지들은 Kaggle에 업로드 되어있다.
[![Kaggle][이미지 예시]](https://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/EDA2.jpg?raw=truehttps://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/Kaggle.png?raw=true)
<a href="https://www.kaggle.com/jangbyeonghui/visually-impairedwhitecane">Visually impaired(whitecane)</a>


<!-- Performance -->

## Performance

### 학습 평가 지표
[![Yolov5 평가지표][그래프 종합]](https://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/results.png?raw=true){: width="200" height="100"}
### 라즈베리파이4 환경
[![라즈베리파이 이미지][실제 구동 이미지]](https://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/%EC%BA%A1%EC%B2%98.PNG?raw=true)

[![라즈베리파이 이미지][실제 구동 gif]](https://github.com/jangByeongHui/OpenSourceSWProject/blob/master/readme_img/action_stream_Trim_Trim_Trim.gif?raw=true)

<!-- conclusion -->

## conclusion
시각장애인들이 휴대하는 흰 지팡이를 높은 정확도로 탐지해낼 수 있었다. 단순 이미지 뿐 아니라 영상에서도 흰 지팡이를 탐지할 수 있었으며 실시간으로는 평균 80~110 fps에서 흰 지팡이를 탐지해냈다. Pre-trained model들에 mAP보다 직접 학습시킨 가중치로 더 높은 AP를 얻어냈다. 또한 보통 실시간 객체 탐지는 30 fps 이상을 달성하면 실시간 객체 탐지의 요건을 충족했다고 평가하는데 우리 모델은 GPU환경에서 30 fps를 훨씬 상회하는 결과를 얻어냈다. 라즈베리파이에서 필요한 패키지를 최소화 함으로서 YOLOv5를 구동하였지만, 실시간 영상 촬영과  실시간 객체 탐지를 동시에 라즈베리파이에서 동작하기에는 어려움이 있었다. 그러나 이를 실시간 스트리밍식으로 바꾸고 라즈베리파이에서 송출하는 영상을 다른 컴퓨터에서 객체 탐지를 함으로서 하드웨어적인 제약을 극복할 수 있었다.



  



  
  
  
  
  
  
  

