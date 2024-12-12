// place files you want to import through the `$lib` alias in this folder.

//アクセス制限
import { isAuthenticated } from '../routes/(shop)/shop/store';

import { get } from 'svelte/store';
import { page } from '$app/stores';
import { control } from '../routes/(shop)/shop/store';

export async function checkSession() {
  try {
    const response = await fetch('/api/whoami', {
      credentials: 'include'  // クッキーを送信するために必要
    });
    if (response.ok) {
      isAuthenticated.set(true);
      return true;
    }
  } catch (error) {
    isAuthenticated.set(false);
  }
  return false;
}

// /shop/controlにアクセスしているときにtrue
//　戻るボタンように作成した
// export function updateControlState() {
//   const currentPath = get(page).url.pathname;
//   if (currentPath.startsWith('/shop/control/itemlist')) {
//     control.set(true);
//     return true;
//   } 
//   if (currentPath.startsWith('/shop/control/orderlist')) {
//     control.set(true);
//     return true;
//   }
//   if (currentPath.startsWith('/shop/control/org-edit')) {
//     control.set(true);
//     return true;
//   }
//   if (currentPath.startsWith('/shop/control/shoplist')) {
//     control.set(true);
//     return true;
//   }
//   else{
//     control.set(false);
//     return false;
//   }
// }
