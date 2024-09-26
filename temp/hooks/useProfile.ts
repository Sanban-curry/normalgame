'use client';

import { useState, useEffect } from 'react';
import { User, Profile, PlayHistory } from '../types';
import { supabase } from '../lib/supabase';

interface UseProfileReturn {
  profile: Profile | null;
  isLoading: boolean;
  error: Error | null;
  updateProfile: (updatedProfile: Partial<Profile>) => Promise<void>;
  playHistory: PlayHistory[];
  fetchPlayHistory: () => Promise<void>;
}

export default function useProfile(userId: string): UseProfileReturn {
  const [profile, setProfile] = useState<Profile | null>(null);
  const [isLoading, setIsLoading] = useState<boolean>(true);
  const [error, setError] = useState<Error | null>(null);
  const [playHistory, setPlayHistory] = useState<PlayHistory[]>([]);

  useEffect(() => {
    fetchProfile();
  }, [userId]);

  const fetchProfile