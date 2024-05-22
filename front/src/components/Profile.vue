<template>

    <div>
      <h2>My Profile</h2>
      <!-- 프로필 정보를 보여주는 내용 -->
    </div>
  </template>
  
  <script>
  export default {
    name: "Profile",
    data() {
      return {
        // 프로필 데이터를 여기에 저장
        profile: {}
      };
    },
    created() {
      // 프로필 데이터를 API를 통해 가져오기
      this.fetchProfile();
    },
    methods: {
      fetchProfile() {
        // API 호출 코드
      }
    }
  };
  </script>
  
  <style scoped>
  /* 스타일을 여기에 작성 */
  </style>
  