import { NextResponse } from 'next/server';
import { createRouteHandlerClient } from '@supabase/auth-helpers-nextjs';
import { cookies } from 'next/headers';
import { Database } from '@/types/supabase';

export async function GET(request: Request) {
  const supabase = createRouteHandlerClient<Database>({ cookies });
  const { searchParams } = new URL(request.url);
  const action = searchParams.get('action');

  const { data: { user } } = await supabase.auth.getUser();

  if (!user) {
    return NextResponse.json({ error: 'Unauthorized' }, { status: 401 });
  }

  switch (action) {
    case 'profile':
      return await getProfile(supabase, user.id);
    case 'history':
      return await