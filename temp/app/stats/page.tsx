import Header from '@/components/Header'
import Footer from '@/components/Footer'
import StatsDisplay from '@/components/StatsDisplay'
import { getStats } from '@/app/api/statistics/route'

export const metadata = {
  title: 'NormaBowl - 統計情報',
  description: 'お茶碗の盛り型に関する統計情報を表示します。',
}

async function StatsPage() {
  const stats = await getStats()

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-3xl font-bold mb-6">統計情報</h1>
        <StatsDisplay stats={stats} />
      </main>
      <Footer />
    </div>
  )
}

export default StatsPage