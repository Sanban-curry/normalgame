'use client';

import React, { useState, useEffect } from 'react';
import { User, Bowl } from '@/types';
import { supabase } from '@/lib/supabase';
import { Edit2, Save } from 'lucide-react';

type ProfileInfoProps = {
  userId: string;
};

const ProfileInfo: React.FC<ProfileInfoProps> = ({ userId }) => {
  const [user, setUser] = useState<User | null>(null);
  const [stats, setStats] = useState<{ averageScore: number; playCount: number } | null>(null);
  const [isEditing, setIsEditing] = useState(false);
  const [editedUsername, setEditedUsername] = useState('');

  useEffect(() => {
    fetchUserData();
    fetchUserStats();
  }, [userId]);

  const fetchUserData = async () => {
    const { data, error } = await supabase
      .from('users')
      .select('*')
      .eq('id', userId)
      .single();

    if (error) {
      console