import { Metadata } from 'next'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import ProfileDisplay from '@/components/ProfileDisplay'
import { getUserProfile } from '@/app/api/users/route'
import { getAchievements } from '@/app/api/achievements/route'
import { getPlayHistory } from '@/app/api/selections/route'

export const metadata: Metadata = {
  title: 'ユーザープロフィール | NormaBowl',
  description: 'NormaBowlのユーザープロフィールページです。個人統計、獲得バッジ、プレイ履歴を確認できます。',
}

async function getProfileData() {
  const userProfile = await getUserProfile()
  const achievements = await getAchievements()
  const playHistory = await getPlayHistory()

  return {
    userProfile,
    achievements,
    playHistory,
  }
}

export default async function ProfilePage() {
  const {