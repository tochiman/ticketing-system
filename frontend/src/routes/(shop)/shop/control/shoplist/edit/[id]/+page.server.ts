import type { PageServerLoad } from './$types';

export const load: PageServerLoad = async ({ params, fetch }) => {
  try {
    // 店舗の詳細情報を取得
    const storeDetailResponse = await fetch(`/api/org/store/${params.id}`);
    if (!storeDetailResponse.ok) {
      throw new Error('Failed to fetch store details');
    }
    const storeDetail = await storeDetailResponse.json();

    return {
      shopData: {
        name: storeDetail.name,
        password: "********", // パスワードは安全のため表示しません
        address: storeDetail.address,
        email: storeDetail.email,
        phone: storeDetail.phone,
        openTime: storeDetail.openTime,
        closeTime: storeDetail.closeTime
      }
    };
  } catch (error) {
    return {
      error: error instanceof Error ? error.message : 'An unknown error occurred'
    };
  }
};
