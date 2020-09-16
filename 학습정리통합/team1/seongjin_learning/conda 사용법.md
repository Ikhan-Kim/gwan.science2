# conda 사용법





설치된 가상환경 리스트 확인

conda info --envs



가상환경 생성

conda create -n 가상환경명 python=version



가상환경 활성화

activate 가상환경명



가상환경 비활성화

deactivate 가상환경명



가상환경 삭제

conda remove --name 가상환경명 --all 

또는

conda remobe -n 가상환경명 --all





인덱스 캐시, 잠긴파일, 사용하지 않는 패키지, 소스 캐시 등 삭제

conda clean --all 또는 conda clean -a



