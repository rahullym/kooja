// S3-compatible media storage (Neon Object Storage in production), wrapping
// EmDash's S3 adapter. Reads S3_* first, then the AWS_* / TIGRIS_* names other
// providers use. Values are read at runtime, never baked into the build.
import { createStorage as createS3Storage } from "emdash/storage/s3";

const first = (...keys: string[]) => keys.map((k) => process.env[k]).find(Boolean);

export const storageBucket = () =>
	first("S3_BUCKET", "TIGRIS_BUCKET_NAME", "TIGRIS_STORAGE_BUCKET", "BUCKET_NAME");

export function createStorage(config: Record<string, unknown>) {
	return createS3Storage({
		endpoint: first("S3_ENDPOINT", "AWS_ENDPOINT_URL_S3", "AWS_ENDPOINT_URL") ?? "https://t3.storage.dev",
		bucket: storageBucket(),
		accessKeyId: first("S3_ACCESS_KEY_ID", "TIGRIS_STORAGE_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID"),
		secretAccessKey: first("S3_SECRET_ACCESS_KEY", "TIGRIS_STORAGE_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY"),
		region: first("S3_REGION", "AWS_REGION") ?? "auto",
		publicUrl: first("S3_PUBLIC_URL"),
		...config,
	});
}
