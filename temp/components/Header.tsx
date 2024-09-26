'use client';

import React, { useState } from 'react';
import Link from 'next/link';
import { Menu, X, User } from 'lucide-react';

const Header = () => {
  const [isMenuOpen, setIsMenuOpen] = useState(false);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-3">
        <div className="flex items-center justify-between">
          {/* ロゴ */}
          <Link href="/" className="text-2xl font-bold text-blue-600">
            NormaBowl
          </Link>

          {/* デスクトップナビゲーション */}
          <nav className="hidden md:flex space-x-4">
            <Link href="/game" className="text-gray-600 hover:text-blue-600">
              ゲーム
            </Link>
            <Link href="/leaderboard"