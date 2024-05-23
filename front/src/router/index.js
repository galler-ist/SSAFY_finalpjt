import { createRouter, createWebHistory } from 'vue-router'
import ArticleView from '@/views/ArticleView.vue'
import DetailView from '@/views/DetailView.vue'
import CreateView from '@/views/CreateView.vue'
import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import HomeView from '@/views/HomeView.vue'
import BankView from '@/views/BankView.vue'
import ExchangeView from '@/views/ExchangeView.vue'
import UpdateView from '@/views/UpdateView.vue'
import FinanceView from '@/views/FinanceView.vue'
import DepositList from '@/components/DepositList.vue'
import SavingList from '@/components/SavingList.vue'
import PortfolioView from '@/views/PortfolioView.vue'
import PortfolioList from '@/components/PortfolioList.vue'
import PortfolioEdit from '@/components/PortfolioEdit.vue'
import Profile from '@/components/Profile.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'HomeView',
      component: HomeView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles/:id',
      name: 'DetailView',
      component: DetailView
    },
    {
      path: '/create',
      name: 'CreateView',
      component: CreateView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/articles/:id/update',
      name: 'UpdateView',
      component: UpdateView
    },
    {
      path: '/bank',
      name: 'BankView',
      component: BankView
    },
    {
      path: '/exchange',
      name: 'ExchangeView',
      component: ExchangeView
    },
    {
      path: '/finance',
      name: 'FinanceView',
      component: FinanceView,
      children: [
        {
          path: 'deposit',
          name: 'DepositList',
          component: DepositList
        },
        {
          path: 'saving',
          name: 'SavingList',
          component: SavingList
        }
      ]
    },
    {
      path: '/finance',
      redirect: '/finance/deposit'
    },
    {
      path: '/portfolio',
      name: 'PortfolioView',
      component: PortfolioView,
      children: [
        {
          path: 'portfoliolist',
          name: 'PortfolioList',
          component: PortfolioList
        },
        {
          path: 'portfolioedit/:id?',
          name: 'PortfolioEdit',
          component: PortfolioEdit
        },
        {
          path: 'profile',
          name: 'Profile',
          component: Profile,
        }
      ]
    },
    {
      path: '/portfolio',
      redirect: '/portfolio/portfoliolist'
    },

  ]
})

import { useCounterStore } from '@/stores/counter'


router.beforeEach((to, from) => {
  const store = useCounterStore()
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요해요!!')
    return { name: 'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'ArticleView' }
  }
})

export default router
