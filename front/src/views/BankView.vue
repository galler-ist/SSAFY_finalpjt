<template>
    <img class="bg" src="/assets/map_bg.png" alt="...">

    <div>
      <h1>카카오 지도 예제</h1>
      <form id="filter-form" @submit.prevent="searchBank">
        <label for="city">지역1:</label>
        <select v-model="city" id="city">
          <option value="서울특별시">서울특별시</option>
          <option value="부산광역시">부산광역시</option>
          <!-- 다른 지역1 추가 -->
        </select>
        <label for="district">지역2:</label>
        <select v-model="district" id="district">
          <option v-for="district in districts" :key="district"  :value="district">{{ district }}</option>
          <!-- 다른 지역 추가 -->
        </select>
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
        <button type="submit">검색</button>
      </form>
      <div id="map" class="map"></div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        city: '서울특별시',
        district: '중구',
        name: '',
        map: null,
        markers: [],
        districts: [],
        seoulDistricts: [
        '강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구',
        '노원구', '도봉구', '동대문구', '동작구', '마포구', '서대문구', '서초구', '성동구',
        '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구'
      ],
      busanDistricts: [
        '강서구', '금정구', '기장군', '남구', '동구', '동래구', '부산진구', '북구',
        '사상구', '사하구', '서구', '수영구', '연제구', '영도구', '중구', '해운대구'
      ]       
      };
    },
    mounted() {
      this.loadKakaoMapScript().then(this.initMap).catch((error) => {
        console.error('Failed to load Kakao Maps API:', error);
      });
      this.updateDistricts();
    },
    watch: {
        city() {
            this.updateDistricts();
        }
    },
    methods: {
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
        if (this.name === '') {
            alert('은행을 선택해주세요');
            return;
        }

        const query = `${this.city} ${this.district} ${this.name}`;
        fetch(`https://dapi.kakao.com/v2/local/search/keyword.json?query=${encodeURIComponent(query)}`, {
          headers: {
            'Authorization': 'KakaoAK 053d9b9ffc2deb571c11f5fb73bdbeb2'
          }
        })
        .then(response => response.json())
        .then(data => {
          if (data.documents && data.documents.length > 0) {
            const filteredDocuments = data.documents.filter(bank => bank.address_name.includes(this.district));
            if (filteredDocuments.length === 0) {
                alert('선택한 지역과 은행에 대한 결과가 없습니다.');
                return;
            }

            this.clearMarkers();
            let activeInfoWindow = null;

            filteredDocuments.forEach(bank => {
              const markerPosition = new kakao.maps.LatLng(bank.y, bank.x);
              const marker = new kakao.maps.Marker({
                position: markerPosition,
                title: bank.place_name,
                clickable: true
              });

              // 인포윈도우 생성
              var infowindow = new kakao.maps.InfoWindow({
                content: `<div style="padding:5px; max-width: 300px;">${bank.place_name}<br>${bank.address_name}</div>`,
                removable: true
              });

              // 마커 클릭 이벤트 리스너 등록

              kakao.maps.event.addListener(marker, 'click', function() {
                if (activeInfoWindow  && activeInfoWindow !== infowindow) {
                    activeInfoWindow.close();
                }
                infowindow.open(this.map, marker);
                activeInfoWindow = infowindow;
              }.bind(this));

              marker.setMap(this.map);
              this.markers.push(marker);
            });

            this.map.setCenter(new kakao.maps.LatLng(filteredDocuments[0].y, filteredDocuments[0].x));
            this.map.setLevel(6); // 지도 확대 레벨
          } else {
            alert('선택한 지역과 은행에 대한 결과가 없습니다.');
          }
        })
        .catch(error => {
          console.error('There has been a problem with your fetch operation:', error);
        });
      },
      clearMarkers() {
        if (this.markers.length > 0) {
          this.markers.forEach(marker => marker.setMap(null));
          this.markers = [];
        }
      },
      updateDistricts() {
        if (this.city === '서울특별시') {
            this.districts = this.seoulDistricts;
            this.district = this.seoulDistricts[23];
        } else if (this.city === '부산광역시') {
            this.districts = this.busanDistricts;
            this.district = this.busanDistricts[0];
        } else {
            this.districts = [];
            this.district = '';
        }
      }
    }
  };
  </script>
  
  <style scoped>
  .map {
    width: 100%;
    height: 1000px;
    padding: 300px;
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