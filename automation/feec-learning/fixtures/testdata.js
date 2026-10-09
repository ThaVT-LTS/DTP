// Dữ liệu dùng chung. Mã dự án và từ khóa tìm kiếm phụ thuộc môi trường dev.
export const PROJECT_ID = process.env.PROJECT_ID ?? '1';
export const DOCUMENTS_URL = `/projects/${PROJECT_ID}/documents`;
export const PROJECTS_URL = '/projects';

export const EXISTING_PROJECT_KEYWORD = 'K2205248 ＮＲＴ０７８ 平井';

// Tên duy nhất cho mỗi lần chạy, tránh trùng dữ liệu cũ.
export const uniqueName = (prefix = 'AUTO') => `${prefix}-${Date.now()}`;
