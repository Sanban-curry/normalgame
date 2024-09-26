'use client';

import React, { useState } from 'react';
import { Bowl } from '@/types';

interface BowlSelectorProps {
  onSelect: (bowl: Bowl) => void;
}

const BowlSelector: React.FC<BowlSelectorProps> = ({ onSelect }) => {
  const [selectedBowl, setSelectedBowl] = useState<Bowl | null>(null);

  const bowls: Bowl[] = [
    { id: 1, name: '少なめ', description: '控えめな盛り付け' },
    { id: 2, name: '普通', description: '一般的な盛り付け' },
    { id: 3, name: '多め', description: 'やや多めの盛り付け'