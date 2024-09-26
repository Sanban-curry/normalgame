'use client';

import React, { useState, useEffect } from 'react';
import { Bowl, ArrowRight, Check } from 'lucide-react';

const GameInterface: React.FC = () => {
  const [selectedBowl, setSelectedBowl] = useState<number | null>(null);
  const [gameStage, setGameStage] = useState<number>(0);
  const [isAnimating, setIsAnimating] = useState<boolean>(false);

  const bowlTypes = [1, 2, 3, 4, 5];

  useEffect(() => {
    if (gameStage === 1) {
      setIsAnimating(true);
      const timer = setTimeout(() => {
        setIsAnimating(false);
        setGameStage(2);
      }, 2000);