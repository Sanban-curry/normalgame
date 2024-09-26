'use client';

import { useState, useEffect } from 'react';
import { useSupabaseClient } from '@supabase/auth-helpers-react';
import { Database } from '../types/supabase';

type BowlType = 1 | 2 | 3 | 4 | 5;

interface GameState {
  playerSelection: BowlType | null;
  averageSelection: BowlType | null;
  score: number;
  feedback: string;
}

export function useGame() {
  const [gameState, setGameState] = useState<GameState>({
    playerSelection: null,
    averageSelection: null,
    score: 0,
    feedback: '',
  });
  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const supabase = useSupabaseClient<Database>();

  const selectBowl = async (bowlType: Bowl