import Link from 'next/link'
import Header from '../components/Header'
import Footer from '../components/Footer'

async function getLatestStatistics() {
  const res = await fetch('http://localhost:3000/api/statistics', { cache: 'no-store' })
  if (!res.ok) {
    throw new Error('Failed to fetch statistics')
  }
  return res.json()
}

export default async function Home() {
  const statistics = await getLatestStatistics()

  return (
    <div className="min-h-screen flex flex-col">
      <Header />
      
      <main className="flex-grow container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold text-center mb-8">NormaBowl - お茶碗の盛り型で「普通」を再発見するゲーム</h1>
        
        <section className="mb-12">
          <h2 className="text-2xl font-semibold mb-