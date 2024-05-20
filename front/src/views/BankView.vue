<template>
    <img class="bg" src="/assets/map_bg.png" alt="...">

    <div class="bank-container">
      <h1>카카오 지도 예제</h1>
      <button @click="showCurrentLocation">현재 나의 위치로 보기</button>
      <form id="filter-form" @submit.prevent="searchBank">
        <a>지역선택 </a>
        <select v-model="selectedCity" @change="updateDistricts">
          <option value="">:: 시/도 ::</option>
          <option v-for="city in cities" :key="city" :value="city">{{ city }}</option>
        </select>
        &nbsp;
        <!-- <label for="district">지역2:</label> -->
        <select v-model="selectedDistrict">
          <option value="">:: 시/군/구 ::</option>
          <option v-for="district in districts" :key="district"  :value="district">{{ district }}</option>
          <!-- 다른 지역 추가 -->
        </select>
        &nbsp;
        <label for="name">은행:</label>
        <select v-model="name" id="name">
            <option value="">-----</option>
            <option value="경남은행">경남은행</option>
            <option value="광주은행">광주은행</option>
            <option value="국민은행">국민은행</option>
            <option value="기업은행">기업은행</option>
            <option value="대구은행">대구은행</option>
            <option value="농협은행">농협은행</option>
            <option value="부산은행">부산은행</option>
            <option value="산업은행">산업은행</option>
            <option value="수협은행">수협은행</option>
            <option value="신한은행">신한은행</option>
            <option value="우리은행">우리은행</option>
            <option value="제주은행">제주은행</option>
            <option value="제일은행">제일은행</option>
            <option value="전북은행">전북은행</option>
            <option value="하나은행">하나은행</option>
            <option value="한국씨티은행">한국씨티은행</option>

          <!-- 다른 은행 추가 -->
        </select>
        &nbsp;
        <button type="submit">검색</button>
      </form>
      <br>
      <div id="map" class="map"></div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        selectedCity: '서울특별시',
        selectedDistrict: '',
        name: '',
        map: null,
        markers: [],
        infoWindows: [],
        districts: [],
        cities: [
        '서울특별시', '부산광역시', '대구광역시', '인천광역시', '광주광역시',
        '대전광역시', '울산광역시', '세종특별자치시', '경기도', '강원특별자치도',
        '충청북도', '충청남도', '전북특별자치도', '전라남도', '경상북도',
        '경상남도', '제주특별자치도'
      ],
      cityDistricts: {
        '서울특별시': [
        '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
        '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
        '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
        ],
       '부산광역시': [
        '강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구',
        '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'
        ],
        '대구광역시': [
          '남구', '달서구', '달성군', '동구', '북구', '서구', '수성구', '중구'
        ],
        '인천광역시': [
          '계양구', '미추홀구', '남동구', '동구', '부평구', '서구', '연수구', '중구', '강화군', '옹진군'
        ],
        '광주광역시': [
          '광산구', '남구', '동구', '북구', '서구'
        ],
        '대전광역시': [
          '대덕구', '동구', '서구', '유성구', '중구'
        ],
        '울산광역시': [
          '남구', '동구', '북구', '울주군', '중구'
        ],
        '세종특별자치시': [
          '세종시'
        ],
        '경기도': [
          '가평군', '고양시 덕양구', '고양시 일산동구', '고양시 일산서구', '과천시', '광명시', '광주시',
          '구리시', '군포시', '김포시', '남양주시', '동두천시', '부천시', '성남시 분당구', '성남시 수정구',
          '성남시 중원구', '수원시 권선구', '수원시 영통구', '수원시 장안구', '수원시 팔달구', '시흥시',
          '안산시 단원구', '안산시 상록구', '안성시', '안양시 동안구', '안양시 만안구', '양주시', '양평군',
          '여주시', '연천군', '오산시', '용인시 기흥구', '용인시 수지구', '용인시 처인구', '의왕시', '의정부시',
          '이천시', '파주시', '평택시', '포천시', '하남시', '화성시'
        ],
        '강원특별자치도': [
          '강릉시', '고성군', '동해시', '삼척시', '속초시', '양구군', '양양군', '영월군',
          '원주시', '인제군', '정선군', '철원군', '춘천시', '태백시', '평창군', '홍천군',
          '화천군', '횡성군'
        ],
        '충청북도': [
          '괴산군', '단양군', '보은군', '영동군', '옥천군', '음성군', '제천시', '증평군', '진천군', '청주시 상당구',
          '청주시 서원구', '청주시 청원구', '청주시 흥덕구', '충주시'
        ],
        '충청남도': [
          '계룡시', '공주시', '금산군', '논산시', '당진시', '보령시', '부여군', '서산시', '서천군', '아산시',
          '연기군', '예산군', '천안시 동남구', '천안시 서북구', '청양군', '태안군', '홍성군'
        ],
        '전북특별자치도': [
          '고창군', '군산시', '김제시', '남원시', '무주군', '부안군', '순창군', '완주군', '익산시', '임실군',
          '장수군', '전주시 덕진구', '전주시 완산구', '정읍시', '진안군'
        ],
        '전라남도': [
          '강진군', '고흥군', '곡성군', '광양시', '구례군', '나주시', '담양군', '목포시', '무안군', '보성군',
          '순천시', '신안군', '여수시', '영광군', '영암군', '완도군', '장성군', '장흥군', '진도군', '함평군',
          '해남군', '화순군'
        ],
        '경상북도': [
          '경산시', '경주시', '고령군', '구미시', '군위군', '김천시', '문경시', '봉화군', '상주시', '성주군',
          '안동시', '영덕군', '영양군', '영주시', '영천시', '예천군', '울릉군', '울진군', '의성군', '청도군',
          '청송군', '칠곡군', '포항시 남구', '포항시 북구'
        ],
        '경상남도': [
          '거제시', '거창군', '고성군', '김해시', '남해군', '밀양시', '사천시', '산청군', '양산시', '의령군',
          '진주시', '창녕군', '창원시 마산합포구', '창원시 마산회원구', '창원시 성산구', '창원시 의창구', '창원시 진해구',
          '통영시', '하동군', '함안군', '함양군', '합천군'
        ],
        '제주특별자치도': [
          '서귀포시', '제주시'
        ]
      }

      };
    },
    mounted() {
      this.updateDistricts();
      this.loadKakaoMapScript().then(this.initMap).catch((error) => {
        console.error('Failed to load Kakao Maps API:', error);
      });
    },
    watch: {
        city() {
            this.updateDistricts();
        }
    },
    methods: {
      showCurrentLocation() {
      if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(position => {
          const lat = position.coords.latitude;
          const lng = position.coords.longitude;
          const currentPosition = new kakao.maps.LatLng(lat, lng);

          // 지도 중심을 현재 위치로 이동
          this.map.setCenter(currentPosition);
          this.map.setLevel(4);

          // 기존 마커가 있으면 제거
          if (this.currentMarker) {
            this.currentMarker.setMap(null);
          }

          // 현재 위치에 마커 추가
          this.currentMarker = new kakao.maps.Marker({
            position: currentPosition,
            map: this.map
          });

          // 인포윈도우 추가
          const infoWindow = new kakao.maps.InfoWindow({
            content: '<div style="padding:5px;">당신의 위치입니다</div>',
            removable: true
          });
          infoWindow.open(this.map, this.currentMarker);
        }, error => {
          console.error('Error occurred while retrieving location:', error);
          alert('현재 위치를 가져올 수 없습니다.');
        });
      } else {
        alert('Geolocation을 사용할 수 없습니다.');
      }
    },

      updateDistricts() {
        this.districts = this.cityDistricts[this.selectedCity] || [];
        this.selectedDistrict = this.districts.length > 0 ? this.districts[0] : '';
      },


      loadKakaoMapScript() {
        return new Promise((resolve, reject) => {
          if (typeof kakao !== 'undefined' && kakao.maps) {
            resolve();
            return;
          }
  
          const script = document.createElement('script');
          script.src = `https://dapi.kakao.com/v2/maps/sdk.js?appkey=98ddec0c92a6954c9df64f11e641b082&autoload=false`;
          script.onload = () => {
            kakao.maps.load(() => {
              if (typeof kakao !== 'undefined' && kakao.maps && kakao.maps.LatLng) {
                resolve();
              } else {
                reject(new Error('Kakao Maps API load failed'));
              }
            });
          };
          script.onerror = () => reject(new Error('Kakao Maps API load failed'));
          document.head.appendChild(script);
        });
      },
      initMap() {
        if (typeof kakao === 'undefined' || typeof kakao.maps === 'undefined' || typeof kakao.maps.LatLng === 'undefined') {
          console.error('Kakao Maps API is not loaded properly.');
          return;
        }
  
        const container = document.getElementById('map');
        const options = {
          center: new kakao.maps.LatLng(37.5665, 126.9780),
          level: 8
        };
        this.map = new kakao.maps.Map(container, options);
      },
      searchBank() {

        if (this.district === '') {
          alert('시/군/구를 선택해주세요')
        }

        if (this.name === '') {
            alert('은행을 선택해주세요');
            return;
        }

        const query = `${this.selectedCity} ${this.selectedDistrict} ${this.name}`;
        fetch(`https://dapi.kakao.com/v2/local/search/keyword.json?query=${encodeURIComponent(query)}`, {
          headers: {
            'Authorization': 'KakaoAK 053d9b9ffc2deb571c11f5fb73bdbeb2'
          }
        })
        .then(response => {
          if (!response.ok) {
            throw new Error(`HTTP error! status: #{response.status}`);
          }
          return response.json();
        })
        .then(data => {
          console.log('data.documents: ', data.documents)
          if (data.documents && data.documents.length > 0) {
            const filteredDocuments = data.documents.filter(bank => bank.address_name.includes(this.selectedDistrict));
            console.log('filteredDocuments: ', filteredDocuments)
            if (filteredDocuments.length === 0) {
                alert('선택한 지역과 은행에 대한 결과가 없습니다.');
                return;
            }
            this.clearMarkers();
            this.addMarkers(filteredDocuments);

        }})
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
      },
      clearMarkers() {
        this.markers.forEach(marker => marker.setMap(null));
        this.infoWindows.forEach(infoWindow => infoWindow.close());
        this.marrkers = [];
        this.infoWindows = [];
      },
      addMarkers(banks) {
        banks.forEach(bank => {
          const position = new kakao.maps.LatLng(bank.y, bank.x);
          const marker = new kakao.maps.Marker({
            map: this.map,
            position
          });
          const infoWindow = new kakao.maps.InfoWindow({
            content: `<div>${bank.place_name}<br>${bank.address_name}</div>`,
            removable: true
          });
          kakao.maps.event.addListener(marker, 'click', () => {
            this.infoWindows.forEach(infoWin => infoWin.close());
            infoWindow.open(this.map, marker);
          });
          this.markers.push(marker);
          this.infoWindows.push(infoWindow);

          this.map.setCenter(new kakao.maps.LatLng(banks[0].y, banks[0].x));
          this.map.setLevel(6);
        });
      }
    }
  };
  </script>
  
  <style scoped>
  .map {
    width: 80%;
    height: 800px;
    margin: 0 auto;
    border: 1px solid #702828;
  }

  .bank-container {
    text-align: center;
    padding: 0 auto;
  }
  .bg {
    width: 100%;
    height: 20rem;
    opacity: 0.7;
  }
  </style>
  <style>
  .font {
    font-family: 'NPSfont_regular';
  }
  </style>
