// Media storage on Tigris (S3-compatible), wrapping EmDash's S3 adapter.
// Tigris's Vercel integration and its docs use several variable names, so
// read whichever is set. Values are read at runtime, never baked into the build.
import { createStorage as createS3Storage } from "emdash/storage/s3";

const first = (...keys: string[]) => keys.map((k) => process.env[k]).find(Boolean);

export const tigrisBucket = () =>
	first("S3_BUCKET", "TIGRIS_BUCKET_NAME", "TIGRIS_STORAGE_BUCKET", "BUCKET_NAME");

export function createStorage(config: Record<string, unknown>) {
	return createS3Storage({
		endpoint: first("S3_ENDPOINT", "AWS_ENDPOINT_URL_S3", "AWS_ENDPOINT_URL") ?? "https://t3.storage.dev",
		bucket: tigrisBucket(),
		accessKeyId: first("S3_ACCESS_KEY_ID", "TIGRIS_STORAGE_ACCESS_KEY_ID", "AWS_ACCESS_KEY_ID"),
		secretAccessKey: first("S3_SECRET_ACCESS_KEY", "TIGRIS_STORAGE_SECRET_ACCESS_KEY", "AWS_SECRET_ACCESS_KEY"),
		region: first("S3_REGION", "AWS_REGION") ?? "auto",
		publicUrl: first("S3_PUBLIC_URL"),
		...config,
	});
}
