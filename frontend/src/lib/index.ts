// place files you want to import through the `$lib` alias in this folder.

//アクセス制限
import { org,store } from '../routes/(shop)/shop/store';

export async function checkSession() {
  try {
    const response = await fetch('/api/org/me', {
      credentials: 'include'  // クッキーを送信するために必要
    });
    if (response.ok) {
      org.set(true);
      return true;
    }
    
    const response2 = await fetch('/api/store/me', {
        credentials: 'include'  // クッキーを送信するために必要
    });
    if (response2.ok){
        store.set(true);
        return true;
    }
    
  } catch (error) {
    org.set(false);
    store.set(false);
    return false;
  }
}

export async function getCoordinates(address: string) {
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

export function updateCoordinates(latitude: string, longitude: string) {
  if (typeof window !== 'undefined') {
    window.dispatchEvent(new CustomEvent('updateCoordinates', {
      detail: { latitude, longitude }
    }));
  }
}
