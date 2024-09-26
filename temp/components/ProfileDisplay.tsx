// components/ProfileDisplay.tsx
import { notFound } from 'next/navigation'
import Image from 'next/image'
import { createServerComponentClient } from '@supabase/auth-helpers-nextjs'
import { cookies } from 'next/headers'
import type { Database } from '@/types/supabase'

type UserStats = {
  totalGames: number
  averageDeviation: number
  bestScore: number
}

type Achievement = {
  id: string
  name: string
  description: string
  icon: string
}

type PlayHistory = {
  id: string
  date: string
  bowlType: number
  deviation: number
}

async function getProfileData(userId: string) {
  const supabase = createServerComponentClient<Database>({ cookies })