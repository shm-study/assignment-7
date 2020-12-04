# Github를 이용해서 과제를 해봅시다

1. 다음 [github](https://github.com/shm-study/cv-assignment)를 fork(upstream → origin) 해옵니다.
2. 로컬 저장소로 Origin을 `git clone` 합니다. (origin → local)
3. 과제가 있는 branch 뒤에 `/<github_id>` 를 붙인 이름으로 새로운 branch를 생성합니다.  
ex) github id가 crystal인 사람이 `assignment-1` branch에 있는 과제를 제출한다면 작업해야 하는 branch 이름은 `assignment-1/crystal`
4. 작업이 잘 완료되었으면. `git push` 하여 Origin에 정보 저장
5. Pull Request를 통해 과제 제출 완료 (origin → upstream)

### Tip : Upstream에 과제가 갱신되었을 때 Origin에 반영하기

1. 로컬 저장소의 Remote 저장소로 upstream을 추가 (이후 설명은 원격 Repository의 이름이 upstream이라는 전제 하에 서술)
2. upstream 저장소로부터 정보를 가져옴 : `git fetch upstream` 
3. upstream 저장소의 정보를 내 로컬과 합침 : `git merge upstream/<branch_name>`
4. origin 저장소로 push : `git push origin <branch_name>`
