// Dữ liệu dùng chung của dự án. Dữ liệu phụ thuộc môi trường (mã dự án, từ khóa có sẵn) đặt ở đây, có chú thích.
// Tên duy nhất cho mỗi lần chạy, tránh trùng dữ liệu cũ.
export const uniqueName = (prefix = 'AUTO') => `${prefix}-${Date.now()}`;
