'use client';

import { useState, useCallback } from 'react';

interface ErrorState {
  hasError: boolean;
  message: string;
}

interface ErrorHandlerHook {
  error: ErrorState;
  setError: (message: string) => void;
  clearError: () => void;
  reportError: (error: Error) => void;
}

const useErrorHandler = (): ErrorHandlerHook => {
  const [error, setErrorState] = useState<ErrorState>({
    hasError: false,
    message: '',
  });

  const setError = useCallback((message: string) => {
    setErrorState({
      hasError: true,
      message,
    });
  }, []);

  const clearError = useCallback(() => {
    setErrorState({
      hasError: false,
      message: '',
    });
  }, []);