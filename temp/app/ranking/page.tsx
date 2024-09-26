import { Metadata } from 'next'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import RankingList from '@/components/RankingList'

export const metadata: Metadata = {
  title: 'ランキング | NormaBowl',
  description: 'NormaBowlのプレイヤーランキングページです。トッププレイヤーのスコアや達成バッジをチェックしよう！',
}

async function getRankingData() {
  // ここでAPI経由でランキングデータを取得します
  // 実際の実装では、app/api/ranking/route.tsなどを呼び出します
  const res = await fetch('http://localhost:3000/api/ranking', { cache: 'no-store' })
  if (!res.ok) {
    throw new Error('ランキングデータの取得に失敗しました')
  }