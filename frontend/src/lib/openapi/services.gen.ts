// This file is auto-generated by @hey-api/openapi-ts

import { createClient, createConfig, type Options } from '@hey-api/client-fetch';
import type { RootScanGetData, RootScanGetError, RootScanGetResponse } from './types.gen';

export const client = createClient(createConfig());

export class DefaultService {
    /**
     * Root
     */
    public static rootScanGet<ThrowOnError extends boolean = false>(options: Options<RootScanGetData, ThrowOnError>) {
        return (options?.client ?? client).get<RootScanGetResponse, RootScanGetError, ThrowOnError>({
            ...options,
            url: '/scan'
        });
    }
    
}