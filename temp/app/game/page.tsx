'use client'

import { useState, useEffect } from 'react'
import Header from '@/components/Header'
import Footer from '@/components/Footer'
import BowlSelector from '@/components/BowlSelector'
import ComparisonDisplay from '@/components/ComparisonDisplay'
import { Bowl, GameState } from '@/types'

// 仮想データ
const mockData = {
  averageBowl: 3,
  totalPlayers: 1000,
}

export default function GamePage() {
  const [selectedBowl, setSelectedBowl] = useState<Bowl | null>(null)
  const [gameState, setGameState] = useState<GameState>('selecting')
  const [averageBowl, setAverageBowl] = useState<number | null>(null)
  const [totalPlayers, setTotalPlayers] = useState<number | null>(null)

  useEffect(() => {
    // 仮想データを使用するか、APIからデ