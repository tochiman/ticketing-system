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

export async function getCoordinates(address) {
  try {
    const encodedAddress = encodeURIComponent(address);
    const response = await fetch(`https://msearch.gsi.go.jp/address-search/AddressSearch?q=${encodedAddress}`);
    if (response.ok) {
      const data = await response.json();
      if (data && data.length > 0) {
        const [longitude, latitude] = data[0].geometry.coordinates;
        return { latitude, longitude };
      }
    }
  } catch (error) {
    console.error('Error fetching coordinates:', error);
  }
  return null;
}

export function updateCoordinates(latitude, longitude) {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('updateCoordinates', {
      detail: { latitude, longitude }
    }));
  }
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
