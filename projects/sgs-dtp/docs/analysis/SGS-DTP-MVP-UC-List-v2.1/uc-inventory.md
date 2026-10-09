# Kiểm kê UC — lượt 1 (trích xuất nguyên văn)

Nguồn: `SGS_DTP_MVP_Use_Case_List_v2_1_final_confirmation.xlsx` · Sinh bằng `scripts/extract_uc_list.py` · Trường **đậm** = nguyên văn nguồn; trường *nghiêng* = suy ra ở bước phân tích (xem analysis.md).

Độ phủ chiều ngược: 1767/1767 ô có dữ liệu trong file gốc xuất hiện nguyên văn trong file này.

## Số UC theo sheet

| Sheet | Số UC |
|---|---|
| Scope Summary | 0 |
| UC List | 159 |
| Future Release | 40 |
| OOS - Not MVP | 5 |
| Pending Clarification | 0 |
| **Tổng** | **204** |

## Sheet: Scope Summary

Dòng có dữ liệu nhưng không phải UC hay tiêu đề section (chép nguyên văn):

| Dòng | Nội dung |
|---|---|
| R2 | Category: MVP UC List · Count: 156 · Meaning: Use cases proposed for the Taiwan MVP confirmation. · MVP Treatment: Included in Sheet UC List · Primary Basis: Requirement-derived Use Case List + latest customer clarifications, including Review Workflow confirmation and Consultant role scope · Client Action: Confirm scope/use cases |
| R3 | Category: Future Release · Count: 39 · Meaning: Use cases explicitly Phase 2 / low priority, or deferred from the first pilot by customer clarification. · MVP Treatment: Not in MVP · Primary Basis: WBS Phase 2 and/or Q&A deferral; Q&A #21 clarifies Evidence Package concept but does not change its Phase 2 timing · Client Action: Acknowledge for later planning |
| R4 | Category: OOS / Not MVP · Count: 5 · Meaning: Use cases explicitly removed from the MVP by customer confirmation. · MVP Treatment: Excluded from MVP · Primary Basis: Q&A #18 and Q&A #56 · Client Action: Confirm exclusion |
| R5 | Category: Pending Clarification · Count: 0 · Meaning: No standalone use case is currently held pending after Q&A #26 was resolved. · MVP Treatment: None · Primary Basis: Q&A #26 resolved; other open source-Q&A topics remain in the Q&A tracker until confirmed · Client Action: Continue resolving open Q&A items |

_Không có UC._

## Sheet: UC List

Dòng có dữ liệu nhưng không phải UC hay tiêu đề section (chép nguyên văn):

| Dòng | Nội dung |
|---|---|
| R2 | ESt (Hour): =SUM($J3,$J9,$J20,$J26,$J30,$J34,$J46,$J55,$J58,$J69,$J72,$J81,$J85,$J90,$J108,$J112,$J118,$J126,$J137,$J152,$J156,$J164,$J171,$J175,$J178,) |

### 1. Authentication

`UC List!R3` · **ESt (Hour):** `=SUM(J4:J8)`

#### UC-AUTH-001 · Log In to Platform
`UC List!R4`

- **Actor:** All authenticated roles
- **Module/Feature:** Authentication
- **Portal:** Customer Portal & SGS Portal
- **Description:** Authenticate with credentials and enter DTP with the role, tenant and affiliate context resolved for the session.
- **WBS Reference:** CP-01 User login & logout (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 14
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — tất cả 8 vai trò đăng nhập
- *Phát hiện:* —

#### UC-AUTH-002 · Log Out of Platform
`UC List!R5`

- **Actor:** All authenticated roles
- **Module/Feature:** Authentication
- **Portal:** Customer Portal & SGS Portal
- **Description:** Terminate the active session and invalidate the session token.
- **WBS Reference:** CP-01 User login & logout (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 4
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — tất cả 8 vai trò đăng nhập
- *Phát hiện:* —

#### UC-AUTH-003 · Request Password Reset
`UC List!R6`

- **Actor:** All authenticated roles
- **Module/Feature:** Authentication
- **Portal:** Customer Portal & SGS Portal
- **Description:** Request a password reset link when the password cannot be recalled, and set a new password from that link.
- **WBS Reference:** Implicit — CP-01 (P1) — self-service password reset not named; only auth API, password policy, session timeout
- **LTS suggestion:** Phase 2
- **SGS Comments:** Ok. In case reset is needed, team can support the client
- **ESt (Hour):** —
- *Nhóm phạm vi:* B1 — LTS đề xuất P2, SGS đồng ý
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — tất cả 8 vai trò đăng nhập
- *Phát hiện:* F-22

#### UC-AUTH-004 · Change Own Password
`UC List!R7`

- **Actor:** All authenticated roles
- **Module/Feature:** Authentication
- **Portal:** Customer Portal & SGS Portal
- **Description:** Change the current password while authenticated, subject to the SGS password policy.
- **WBS Reference:** Implicit — CP-01 (P1) — change-password not named
- **LTS suggestion:** Phase 2
- **SGS Comments:** Ok. In case reset is needed, team can support the client
- **ESt (Hour):** —
- *Nhóm phạm vi:* B1 — LTS đề xuất P2, SGS đồng ý
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — tất cả 8 vai trò đăng nhập
- *Phát hiện:* F-22

#### UC-AUTH-005 · Activate Account from Invitation
`UC List!R8`

- **Actor:** Customer Admin, Customer User, SGS User, SGS Consultant
- **Module/Feature:** Authentication
- **Portal:** Customer Portal & SGS Portal
- **Description:** Accept a user invitation, set the initial password and complete first-time account activation.
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-04 SGS customer onboarding (P1); Q&A #7; Q&A #59a
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User, SGS Consultant
- *Phát hiện:* F-33

### 2. User & Profile Management

`UC List!R9` · **ESt (Hour):** `=SUM(J10:J19)`

#### UC-USR-001 · View User List
`UC List!R10`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** View the users within the permitted boundary (own tenant for Customer Admin; affiliate customers and SGS users for SGS Admin) with status and role.
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-05 Customer and user administration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* —

#### UC-USR-002 · View User Details
`UC List!R11`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** View a user's profile, account status, assigned role and assigned scopes.
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-05 Customer and user administration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* —

#### UC-USR-003 · Create User and Send Invitation
`UC List!R12`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** Create a user account, assign the initial role and issue an invitation. Includes resending or revoking a pending invitation.
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-05 Customer and user administration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* —

#### UC-USR-004 · Edit User Account
`UC List!R13`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** Update another user's account attributes maintained by an administrator.
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-05 Customer and user administration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* F-22

#### UC-USR-005 · Assign Role to User
`UC List!R14`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** Assign or change the predefined platform role held by a user. Customer Admin manages customer-side roles; SGS Admin manages SGS-side roles, including the SGS Consultant role.
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-05 Customer and user administration (P1); Q&A #59a
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* —

#### UC-USR-006 · Assign Scope Access to Customer User
`UC List!R15`

- **Actor:** Customer Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal
- **Description:** Grant a Customer User access to specific product, system or organizational scopes.
- **WBS Reference:** CP-05 Create and manage customer users (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-31

#### UC-USR-007 · Activate User Account
`UC List!R16`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** Re-enable a previously deactivated user account.
- **WBS Reference:** Implicit — OPS-05 'Reset/disable access' (P1) — re-activation not named
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* —

#### UC-USR-008 · Deactivate User Account
`UC List!R17`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** Disable a user's access while retaining the user record and its history.
- **WBS Reference:** OPS-05 Customer and user administration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* F-22

#### UC-USR-009 · Delete User Account
`UC List!R18`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** —
- **WBS Reference:** CP-05 Create and manage customer users (P1); OPS-05 Customer and user administration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Cờ dữ liệu:* Cột 'Description' trống
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* F-07, F-22

#### UC-USR-010 · Reset User Password
`UC List!R19`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** User Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** Trigger the administrator password-reset flow for another user without exposing the new password to the administrator; a temporary password is issued to the account owner, who must change it on first login.
- **WBS Reference:** OPS-05 Customer and user administration (P1); Q&A #45
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* F-22

### 3. Role & Permission Administration

`UC List!R20` · **ESt (Hour):** `=SUM(J21:J25)`

#### UC-ROL-001 · Enforce Role, Tenant and Affiliate Permissions
`UC List!R21`

- **Actor:** System
- **Module/Feature:** Role & Permission
- **Portal:** System / Backend (No Portal)
- **Description:** Enforce the predefined role and permission matrix on APIs and UI so customer users can access only their organization/scope data and SGS users, including SGS Consultants, can access only customers and functions permitted by their role and assignment boundary.
- **WBS Reference:** CP-03 User roles & permissions management (P1); Q&A #59a
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 36
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-32

#### UC-ROL-002 · View Role Permission Matrix
`UC List!R22`

- **Actor:** Customer Admin, SGS Admin
- **Module/Feature:** Role & Permission
- **Portal:** Customer Portal & SGS Portal
- **Description:** View the read/write/approve/share/admin permissions attached to a role, so administrators can choose the correct role when assigning users.
- **WBS Reference:** PRESALE WBS GAP — CP-03 (P1) 'Define permission matrix per PRD' is a design artefact, not a viewable matrix
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 7
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, SGS Admin
- *Phát hiện:* F-32

#### UC-ROL-003 · Create Role
`UC List!R23`

- **Actor:** SGS Admin
- **Module/Feature:** Role & Permission
- **Portal:** SGS Portal
- **Description:** Define a new role and select its permission set.
- **WBS Reference:** PRESALE WBS GAP — No role authoring in the estimation; FRD assumption 4.3 fixes a 7-role RBAC model
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-ROL-004 · Edit Role Permissions
`UC List!R24`

- **Actor:** SGS Admin
- **Module/Feature:** Role & Permission
- **Portal:** SGS Portal
- **Description:** Modify the permission set of a custom role.
- **WBS Reference:** PRESALE WBS GAP — No permission authoring in the estimation; FRD assumption 4.3 fixes a 7-role RBAC model
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-ROL-005 · Delete Role
`UC List!R25`

- **Actor:** SGS Admin
- **Module/Feature:** Role & Permission
- **Portal:** SGS Portal
- **Description:** Remove a custom role that is no longer assigned to any user.
- **WBS Reference:** PRESALE WBS GAP — No role authoring in the estimation; FRD assumption 4.3 fixes a 7-role RBAC model
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 5. Notification

`UC List!R26` · **ESt (Hour):** `=SUM(J27:J29)`

#### UC-NTF-001 · Generate In-App Notification
`UC List!R27`

- **Actor:** System
- **Module/Feature:** Notification
- **Portal:** System / Backend (No Portal)
- **Description:** Generate role-, tenant- and scope-aware in-app notifications for relevant MVP events such as review feedback, service-request status changes and certification milestones.
- **WBS Reference:** CP-44 In-app notifications (P1); CP-28 Review notifications (P1); CP-35 Service request status flow & notification (P1); CP-42 Cert renewal/surveillance notifications (P1). Email notifications remain P2 under CP-45.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-36

#### UC-NTF-002 · View Notification Inbox and History
`UC List!R28`

- **Actor:** All authenticated roles
- **Module/Feature:** Notification
- **Portal:** Customer Portal & SGS Portal
- **Description:** View current and historical notifications addressed to the user.
- **WBS Reference:** CP-44
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — tất cả 8 vai trò đăng nhập
- *Phát hiện:* —

#### UC-NTF-003 · Manage Notification Templates and Events
`UC List!R29`

- **Actor:** SGS Admin
- **Module/Feature:** Notification
- **Portal:** SGS Portal
- **Description:** Maintain notification templates and the mapping of platform events to templates and recipient rules.
- **WBS Reference:** OPS-23 Platform notifications admin (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 6. Audit Trail

`UC List!R30` · **ESt (Hour):** `=SUM(J31:J33)`

#### UC-AUD-001 · Record Audit Trail Entry
`UC List!R31`

- **Actor:** System
- **Module/Feature:** Audit Trail
- **Portal:** System / Backend (No Portal)
- **Description:** Record append-only audit events for sensitive platform, review and service-request actions with actor, timestamp, action and affected object/context.
- **WBS Reference:** CP-47 Audit log (platform) (P1); OPS-17 Review audit log (P1); OPS-19 Service request audit log (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 20
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-36, F-37

#### UC-AUD-002 · Search and View Audit Trail
`UC List!R32`

- **Actor:** SGS Admin
- **Module/Feature:** Audit Trail
- **Portal:** SGS Portal
- **Description:** Search platform audit events by actor, object, action, date range and tenant for support, compliance and investigation.
- **WBS Reference:** CP-47 Audit log (platform) (P1)
- **LTS suggestion:** —
- **SGS Comments:** Phase 2?
- **ESt (Hour):** —
- *Nhóm phạm vi:* E — không có đề xuất, không có giờ
- *Xử lý test:* Chưa xác định – chờ Q-13
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-14, F-37

#### UC-AUD-004 · View Own Organization Activity Log
`UC List!R33`

- **Actor:** Customer Admin
- **Module/Feature:** Audit Trail
- **Portal:** Customer Portal
- **Description:** Review activity performed on the organization's own evidence, certifications and users.
- **WBS Reference:** PRESALE WBS GAP — CP-47 (P1) is scoped to SGS Admin; no customer-facing activity log priced
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-37

### 7. Framework Content Management

`UC List!R34` · **ESt (Hour):** `=SUM(J35:J45)`

#### UC-FWK-001 · View Framework List
`UC List!R35`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** View the frameworks maintained on the platform and open their current framework content.
- **WBS Reference:** A5 Framework dynamic management (P1); OPS-07 Framework and cert configuration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-FWK-002 · View Framework Details
`UC List!R36`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** View a framework's metadata, requirement/control structure and expected evidence types. Frameworks are managed independently in MVP; no ISO 27001/42001 cross-framework requirement/control equivalence mapping is included.
- **WBS Reference:** A5 Framework dynamic management (P1); OPS-07 Framework and cert configuration (P1); Q&A #18 cross-framework mapping OOS for MVP
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-FWK-003 · Create Framework
`UC List!R37`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Register a new framework with its metadata and structural definition.
- **WBS Reference:** A5 Framework dynamic management (P1); OPS-07 Framework and cert configuration (P1)
- **LTS suggestion:** move back to P1
- **SGS Comments:** ISO27001, ISO42001 and / CMS should be initially supported
- **ESt (Hour):** —
- *Nhóm phạm vi:* D — LTS ghi 'move back to P1', chưa có giờ
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-13, F-35

#### UC-FWK-004 · Edit Framework Metadata
`UC List!R38`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Modify framework-level metadata and structure supported by the framework data model.
- **WBS Reference:** A5 Framework dynamic management (P1); OPS-07 Framework and cert configuration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-36

#### UC-FWK-005 · Create Requirement or Control
`UC List!R39`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Add a requirement or control to a framework, positioned within its clause hierarchy.
- **WBS Reference:** A5 Framework dynamic management (P1); OPS-07 Framework and cert configuration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-24

#### UC-FWK-006 · Edit Requirement or Control
`UC List!R40`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Modify the text, hierarchy position, applicability level or attributes of a requirement or control.
- **WBS Reference:** A5 Framework dynamic management (P1); OPS-07 Framework and cert configuration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-24

#### UC-FWK-007 · Retire Requirement or Control
`UC List!R41`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Withdraw a requirement or control from future use while preserving existing customer evidence mappings.
- **WBS Reference:** PRESALE WBS GAP — Retirement preserving existing evidence mappings not priced; nearest A5 CRUD (P1), A8 migration (P2)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-24

#### UC-FWK-008 · Define Expected Evidence Types for a Control
`UC List!R42`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Define the evidence types expected for a control and flag each as mandatory or optional.
- **WBS Reference:** A5 Framework dynamic management (P1)
- **LTS suggestion:** —
- **SGS Comments:** What are the types of evidences? Files? / This could be shifted to P2
- **ESt (Hour):** 8
- *Nhóm phạm vi:* F — có giờ, SGS gợi ý có thể lùi P2
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-35

#### UC-FWK-009 · Import Framework Content
`UC List!R43`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Import or update SGS-supplied framework content from XLSX, including ISO 27001/42001 requirements/controls and expected evidence types, with each framework maintained independently.
- **WBS Reference:** OPS-07 Framework and cert configuration (P1); Q&A #16/#18 — XLSX input; ISO 27001/42001 cross-framework requirement/control mapping is OUT OF MVP
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 18
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-FWK-013 · Activate Framework
`UC List!R44`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Make a framework version available for discovery, journeys and evidence workspaces.
- **WBS Reference:** PRESALE WBS GAP — Framework availability activation not priced; CP-12 (P1) is customer-side activation on a scope
- **LTS suggestion:** move back to P1
- **SGS Comments:** The framework needs to be available in P1, / otherwise evidence management is useless! Or did I understand it wrong?
- **ESt (Hour):** —
- *Nhóm phạm vi:* D — LTS ghi 'move back to P1', chưa có giờ
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-13, F-26

#### UC-FWK-014 · Deactivate Framework
`UC List!R45`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Portal:** SGS Portal
- **Description:** Withdraw a framework from new use while preserving all historical usage and records.
- **WBS Reference:** PRESALE WBS GAP — Framework deactivation not priced; nearest OPS-07 admin config (P2)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 8. Certification Configuration

`UC List!R46` · **ESt (Hour):** `=SUM(J47:J54)`

#### UC-SCH-001 · View Certification Scheme List
`UC List!R47`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** View the certification schemes configured on the platform.
- **WBS Reference:** Implicit — OPS-07 cert configuration (P2) — no certification scheme entity is named
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-SCH-002 · View Certification Scheme Details
`UC List!R48`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** View a scheme's record structure, permitted statuses, sharing rules and maintenance cycle configuration.
- **WBS Reference:** Implicit — OPS-07 (P2) — no certification scheme entity is named
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-SCH-003 · Create Certification Scheme
`UC List!R49`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** Define a new certification scheme linked to a framework, so certification records can be raised against it.
- **WBS Reference:** PRESALE WBS GAP — No certification scheme object in the estimation; OPS-07 (P2) configures fields on records only
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-SCH-004 · Configure Certification Record Fields and Statuses
`UC List!R50`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** Configure the fields captured on certification records and the permitted certification status values.
- **WBS Reference:** OPS-07 Framework and cert configuration (P1); CP-39 Certification lifecycle statuses (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-16

#### UC-SCH-005 · Configure Certification Sharing Rules
`UC List!R51`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** Configure the certification sharing rules supported by the platform.
- **WBS Reference:** OPS-07 Framework and cert configuration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-SCH-006 · Configure Surveillance and Renewal Cycle Rules
`UC List!R52`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** Define the surveillance interval, renewal lead time and milestone notification offsets for a scheme.
- **WBS Reference:** PRESALE WBS GAP — Surveillance interval / renewal lead-time configuration not priced; CP-42 (P1) prices the alerts but not the rules
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-16

#### UC-SCH-007 · Activate Certification Scheme
`UC List!R53`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** Make a scheme available for new certification records.
- **WBS Reference:** PRESALE WBS GAP — No scheme lifecycle in the estimation
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-SCH-008 · Deactivate Certification Scheme
`UC List!R54`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Scheme
- **Portal:** SGS Portal
- **Description:** Withdraw a scheme from new use while preserving issued certification records.
- **WBS Reference:** PRESALE WBS GAP — No scheme lifecycle in the estimation
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 10. Platform & Tenant Configuration

`UC List!R55` · **ESt (Hour):** `=SUM(J56:J57)`

#### UC-CFG-001 · Configure Platform Settings
`UC List!R56`

- **Actor:** SGS Admin
- **Module/Feature:** Platform Configuration
- **Portal:** SGS Portal
- **Description:** Configure platform-level settings and per-tenant feature toggles so SGS can enable or disable supported modules without a release.
- **WBS Reference:** B3 Platform configuration + feature toggles (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-CFG-002 · Configure Default Evidence Freshness Rules
`UC List!R57`

- **Actor:** SGS Admin
- **Module/Feature:** Platform Configuration
- **Portal:** SGS Portal
- **Description:** Define default freshness periods by framework or evidence type, applied where evidence carries no expiry or review date.
- **WBS Reference:** PRESALE WBS GAP — Default freshness rules by framework/evidence type (PRD RL-07) not priced; CP-16 (P1) uses evidence dates only
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 11. Customer Account Administration

`UC List!R58` · **ESt (Hour):** `=SUM(J59:J68)`

#### UC-ACC-001 · View Customer Account List
`UC List!R59`

- **Actor:** SGS Admin, SGS User, SGS Consultant
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** View customer accounts within the user's permitted SGS affiliate/assignment boundary. SGS Consultants see only customers assigned to them.
- **WBS Reference:** OPS-05 Customer and user administration (P1); Q&A #59f
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin, SGS User, SGS Consultant
- *Phát hiện:* —

#### UC-ACC-002 · View Customer Account Details
`UC List!R60`

- **Actor:** SGS Admin, SGS User, SGS Consultant
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** View a customer account's core profile, affiliate linkage, users and scopes within the permitted boundary. SGS Consultants are limited to their assigned customer.
- **WBS Reference:** OPS-05 Customer and user administration (P1); Q&A #59f
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin, SGS User, SGS Consultant
- *Phát hiện:* —

#### UC-ACC-003 · Create Customer Account and Tenant
`UC List!R61`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Create a customer account and its tenant as part of SGS customer onboarding.
- **WBS Reference:** OPS-04 SGS customer onboarding (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-21

#### UC-ACC-004 · Edit Customer Account
`UC List!R62`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Update SGS-maintained account attributes.
- **WBS Reference:** OPS-05 Customer and user administration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-ACC-005 · Link Customer Account to SGS Affiliate
`UC List!R63`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Assign the customer account to the owning SGS affiliate legal entity, which bounds all SGS-side visibility of that customer.
- **WBS Reference:** CP-03 User roles & permissions management (P1); OPS-05 Customer and user administration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 4
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-40

#### UC-ACC-006 · Assign SGS Personnel to Customer Account
`UC List!R64`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Assign SGS personnel/owners to a customer account within the permitted affiliate boundary. For the SGS Consultant role, allow at most one active Consultant to be assigned to a customer. Automated conflict-of-interest checking is not part of MVP.
- **WBS Reference:** OPS-04 SGS customer onboarding (P1); Q&A #56 — automated COI controls removed from MVP; Q&A #59f — one Consultant per customer, assigned by SGS
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-34

#### UC-ACC-007 · Invite Initial Customer Admin
`UC List!R65`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Create and invite the first Customer Admin for a newly onboarded tenant.
- **WBS Reference:** OPS-04 SGS customer onboarding (P1); Q&A #7
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 4
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-21

#### UC-ACC-008 · Activate Customer Account
`UC List!R66`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Activate an account so its users may access the platform.
- **WBS Reference:** OPS-04 SGS customer onboarding (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-21

#### UC-ACC-009 · Suspend Customer Account
`UC List!R67`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Suspend platform access for an account while retaining all data.
- **WBS Reference:** Implicit — OPS-04 tenant activation status (P1); OPS-05 'disable access' (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-ACC-010 · Offboard Customer Account
`UC List!R68`

- **Actor:** SGS Admin
- **Module/Feature:** Customer Account
- **Portal:** SGS Portal
- **Description:** Close an account and apply the agreed retention, deletion or anonymisation treatment to its data.
- **WBS Reference:** PRESALE WBS GAP — Offboarding with retention / deletion / anonymisation (PRD NFR-PRV-03/04) not priced
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 12. Organization Profile Management

`UC List!R69` · **ESt (Hour):** `=SUM(J70:J71)`

#### UC-ORG-001 · View Organization Profile
`UC List!R70`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Organization Profile
- **Portal:** Customer Portal
- **Description:** View the organization's own profile as held on the platform.
- **WBS Reference:** CP-04 Organization profile management (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-ORG-002 · Edit Organization Profile
`UC List!R71`

- **Actor:** Customer Admin
- **Module/Feature:** Organization Profile
- **Portal:** Customer Portal
- **Description:** Maintain the organization's profile information supported by the platform.
- **WBS Reference:** CP-04 Organization profile management (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

### 13. Scope Management

`UC List!R72` · **ESt (Hour):** `=SUM(J73:J80)`

#### UC-SCP-001 · View Scope List
`UC List!R73`

- **Actor:** Customer Admin, Customer User (+ SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — assigned, read-only)
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** View the product, system and organizational scopes registered by the organization within the permitted customer/assignment boundary.
- **WBS Reference:** CP-06 Manage product/system/org scopes (P1);
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User (xem), SGS Trainer/Assessor (xem), SGS Auditor/Certification (xem), SGS Consultant (xem)
- *Phát hiện:* —

#### UC-SCP-002 · View Scope Details
`UC List!R74`

- **Actor:** Customer Admin, Customer User (+ assigned SGS roles including SGS Consultant, read-only)
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal & SGS Portal
- **Description:** View a scope's definition, obligation level, linked frameworks, workspaces, certifications and related context within the permitted assignment boundary.
- **WBS Reference:** CP-06 Manage product/system/org scopes (P1);
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User (xem), SGS Trainer/Assessor (xem), SGS Auditor/Certification (xem), SGS Consultant (xem) — 'assigned SGS roles' hiểu là SGS User, Trainer/Assessor, Auditor/Certification, Consultant [GIẢ ĐỊNH]
- *Phát hiện:* —

#### UC-SCP-003 · Create Scope
`UC List!R75`

- **Actor:** Customer Admin
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal
- **Description:** Create an organization, product, or system scope. Organization and product are independent peer scopes; a system may belong to both an organization and a product.
- **WBS Reference:** CP-06 Manage product/system/org scopes (P1); Q&A #8
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 7
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-SCP-004 · Edit Scope
`UC List!R76`

- **Actor:** Customer Admin
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal
- **Description:** Update an existing organization, product or system scope.
- **WBS Reference:** CP-06 Manage product/system/org scopes (P1); Q&A #8
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-SCP-005 · Archive Scope
`UC List!R77`

- **Actor:** Customer Admin
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal
- **Description:** Retire a scope from active use while retaining its historical records.
- **WBS Reference:** PRESALE WBS GAP — Archive/retire preserving history not priced; CP-06 CRUD (P1) implies hard delete only
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-23

#### UC-SCP-006 · Link Framework to Scope
`UC List!R78`

- **Actor:** Customer Admin
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal
- **Description:** Attach one or more frameworks to a scope, establishing the obligations to be prepared for and triggering workspace creation.
- **WBS Reference:** CP-06 Manage product/system/org scopes (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-26

#### UC-SCP-007 · Unlink Framework from Scope
`UC List!R79`

- **Actor:** Customer Admin
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal
- **Description:** Withdraw a framework from a scope's active journey while retaining its evidence and review history.
- **WBS Reference:** PRESALE WBS GAP — Unlinking a framework from a scope is not priced
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-23

#### UC-SCP-008 · Define Obligation Coverage Between Scopes
`UC List!R80`

- **Actor:** Customer Admin
- **Module/Feature:** Scope Management
- **Portal:** Customer Portal
- **Description:** Record that an organization-level scope, control or certification supports one or more product- or system-level obligations.
- **WBS Reference:** A1 Organization-level to product/system-level obligation linkage (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

### 14. Customer Cockpit

`UC List!R81` · **ESt (Hour):** `=SUM(J82:J84)`

#### UC-CKP-001 · View Customer Cockpit
`UC List!R82`

- **Actor:** Customer Admin, Customer User, Customer Viewer
- **Module/Feature:** Customer Cockpit
- **Portal:** Customer Portal
- **Description:** View the customer landing dashboard with Digital Trust status, pending actions and a recommended next step across the journey (discovery → training → advisory/readiness assessment → certification).
- **WBS Reference:** CP-07 Customer landing dashboard (P1); Q&A #10
- **LTS suggestion:** Phase 2
- **SGS Comments:** Suggest to be included in P1
- **ESt (Hour):** —
- *Nhóm phạm vi:* B2 — LTS đề xuất P2, SGS muốn giữ P1, chưa có giờ
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer
- *Phát hiện:* F-12, F-19

#### UC-CKP-002 · View Portfolio Matrix
`UC List!R83`

- **Actor:** Customer Admin, Customer User, Customer Viewer
- **Module/Feature:** Customer Cockpit
- **Portal:** Customer Portal
- **Description:** View scopes against journey stages and frameworks in a matrix to compare progress across the portfolio.
- **WBS Reference:** CP-08 Journey Matrix view (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** Suggest to be included in P1
- **ESt (Hour):** —
- *Nhóm phạm vi:* B2 — LTS đề xuất P2, SGS muốn giữ P1, chưa có giờ
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer
- *Phát hiện:* F-12

#### UC-CKP-003 · View Assigned Customer Cockpit
`UC List!R84`

- **Actor:** SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- **Module/Feature:** SGS Cockpit
- **Portal:** SGS Portal
- **Description:** View the trimmed cockpit for an assigned customer, showing only information permitted for the role's customer assignment and access permissions.
- **WBS Reference:** PRESALE WBS GAP — Trimmed SGS Assessor/Auditor cockpit (PRD CC-16, NFR-UX-02); Q&A #59a/#59f extends assigned-customer access to SGS Consultant
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- *Phát hiện:* —

### 15. Customer Journey

`UC List!R85` · **ESt (Hour):** `=SUM(J86:J89)`

#### UC-JRN-001 · View Journey for a Scope
`UC List!R86`

- **Actor:** Customer Admin, Customer User, Customer Viewer (+ assigned SGS roles, read-only)
- **Module/Feature:** Customer Journey
- **Portal:** Customer Portal
- **Description:** View the Discovery → Training → Gap Analysis → Assessment → Audit → Certification journey for a scope, with per-stage status, pending items and entry points into the responsible module.
- **WBS Reference:** CP-09 Journey view (linear stages) (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS User (xem), SGS Trainer/Assessor (xem), SGS Auditor/Certification (xem) — 'assigned SGS roles' hiểu là SGS User, Trainer/Assessor, Auditor/Certification [GIẢ ĐỊNH]
- *Phát hiện:* —

#### UC-JRN-002 · View Framework-Specific Journey Progress
`UC List!R87`

- **Actor:** Customer Admin, Customer User, Customer Viewer
- **Module/Feature:** Customer Journey
- **Portal:** Customer Portal
- **Description:** View journey progress separately per framework where a scope carries several frameworks.
- **WBS Reference:** CP-09 Journey view (linear stages) (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer
- *Phát hiện:* —

#### UC-JRN-003 · View Obligation Coverage Relationship
`UC List!R88`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Customer Journey
- **Portal:** Customer Portal
- **Description:** See where an organization-level control, framework or certification satisfies a product- or system-level obligation.
- **WBS Reference:** A1 Organization-level to product/system-level obligation linkage (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-JRN-004 · Derive Journey Stage Status
`UC List!R89`

- **Actor:** System
- **Module/Feature:** Customer Journey
- **Portal:** System / Backend (No Portal)
- **Description:** Derive each stage's status from readiness, review, service request and certification state, and mark stages not started, in progress, completed, blocked or not applicable.
- **WBS Reference:** Implicit — CP-09 'Stage status labels' (P1) — the derivation rules per stage are not itemised
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

### 17. Evidence Management

`UC List!R90` · **ESt (Hour):** `=SUM(J91:J107)`

#### UC-EVD-001 · Create Evidence Workspace
`UC List!R91`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Manually create an Evidence Workspace for a selected scope and framework for the current certification cycle. Only one workspace may exist for the same scope+framework within a certification cycle.
- **WBS Reference:** CP-13 Evidence workspace creation (P1); Q&A #19
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-27

#### UC-EVD-002 · Create Evidence Workspace on Framework Activation
`UC List!R92`

- **Actor:** System
- **Module/Feature:** Evidence Management
- **Portal:** System / Backend (No Portal)
- **Description:** Automatically create the Evidence Workspace when a framework is activated on a scope, preventing duplicates for the same scope+framework in the current certification cycle. A new certification cycle creates a new workspace.
- **WBS Reference:** CP-13 Evidence workspace creation (P1); Q&A #19
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-26, F-27

#### UC-EVD-003 · View Evidence Workspace List
`UC List!R93`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** View and open the organization's Evidence Workspaces with their scope, framework and certification-cycle context.
- **WBS Reference:** CP-13 Evidence workspace creation (P1); Q&A #19
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-EVD-004 · Browse Controls Catalogue
`UC List!R94`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Browse the requirements and controls of the workspace's framework with their current evidence and declaration state.
- **WBS Reference:** CP-14 Controls catalogue browser (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 9
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-17

#### UC-EVD-005 · View Control Details
`UC List!R95`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** View a control's text, expected evidence types, mapped evidence, maturity declaration and gap flags.
- **WBS Reference:** CP-14 Controls catalogue browser (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-17

#### UC-EVD-006 · View Evidence Library
`UC List!R96`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** View all evidence held by the organization with metadata, mapping summary and status.
- **WBS Reference:** CP-15 Evidence library (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-31

#### UC-EVD-007 · View Evidence Details
`UC List!R97`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** View an evidence item's stored file, metadata, mapped controls, freshness and current evidence/review status.
- **WBS Reference:** CP-15 Evidence library (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-17

#### UC-EVD-008 · Upload Evidence
`UC List!R98`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Upload an evidence file against one or more controls and capture supported metadata such as title, owner, description, version, dates, expiry/review date and comments.
- **WBS Reference:** CP-16 Upload evidence to control (P1); CP-49 Secure evidence document storage (P1); Q&A #54
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 16
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-36

#### UC-EVD-010 · Edit Evidence Metadata
`UC List!R99`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Update an evidence item's metadata, including the dates that drive freshness.
- **WBS Reference:** CP-16 Upload evidence to control (P1); CP-15 Evidence library (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-EVD-011 · Map Evidence to Requirements or Controls
`UC List!R100`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Manually map an existing evidence item to one or more requirements/controls selected by the user, including across frameworks where permitted. Updating shared evidence metadata/expiry applies to all linked controls; no automatic cross-framework control-equivalence mapping is included.
- **WBS Reference:** CP-16 Upload evidence to control (P1); Q&A #20; Q&A #18 — automatic ISO 27001/42001 cross-framework mapping is OUT OF MVP
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-36

#### UC-EVD-012 · Remove Evidence Mapping
`UC List!R101`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Remove a mapping between an evidence item and a control, with the completeness impact reflected.
- **WBS Reference:** CP-15 Evidence library (P1); CP-16 Upload evidence to control (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 4
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-EVD-013 · Replace Evidence with New Version
`UC List!R102`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Supersede an evidence item with an updated version, retaining the prior version and its review history.
- **WBS Reference:** PRESALE WBS GAP — Evidence version supersession is not priced; CP-16 (P1) has 'version' as a metadata field only, not a version chain
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-EVD-014 · Update Evidence Workflow Status
`UC List!R103`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Update evidence workflow status using the MVP status model defined in WBS (draft, submitted for review, reviewed, rejected, accepted or archived), subject to permitted transitions.
- **WBS Reference:** CP-20 Evidence workflow statuses (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-20, F-29, F-36

#### UC-EVD-015 · Delete Evidence
`UC List!R104`

- **Actor:** Customer Admin
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Permanently delete an evidence record and its stored file where retention policy permits, with the deletion recorded in the audit trail.
- **WBS Reference:** CP-15 Evidence library (P1); CP-47 Audit log (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-29, F-36

#### UC-EVD-016 · Assign Requirement Owner
`UC List!R105`

- **Actor:** Customer Admin
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Assign an internal owner to a requirement or control so preparation work and pending actions can be attributed.
- **WBS Reference:** Implicit — CP-17 'owner/comments' on the maturity declaration (P1) — requirement-level owner assignment not named
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-EVD-019 · Archive Evidence Workspace
`UC List!R106`

- **Actor:** Customer Admin
- **Module/Feature:** Evidence Management
- **Portal:** Customer Portal
- **Description:** Close a workspace that is no longer active while retaining its evidence, declarations and review history.
- **WBS Reference:** PRESALE WBS GAP — Workspace closure not priced; CP-20 (P2) archives evidence and packages, not workspaces
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-29

#### UC-EVD-020 · Access Assigned Customer Evidence
`UC List!R107`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- **Module/Feature:** Evidence Management
- **Portal:** SGS Portal
- **Description:** Access the assigned customer's evidence and related requirement/control context within the permitted service/customer assignment. SGS Consultant access supports Implementation Support and Gap Analysis; customer evidence remains maintained through the existing Evidence Management workflow.
- **WBS Reference:** OPS-09 SGS scoped evidence access (P1); Q&A #56 — automated COI controls removed from MVP
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 20
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- *Phát hiện:* F-18

### 18. Self-Assessment & Maturity Declaration

`UC List!R108` · **ESt (Hour):** `=SUM(J109:J111)`

#### UC-ASM-001 · Declare Control Maturity
`UC List!R109`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Self-Assessment
- **Portal:** Customer Portal
- **Description:** Declare control maturity as implemented, partial, not implemented or N/A and capture the owner/comments supported by the WBS.
- **WBS Reference:** CP-17 Maturity self-declaration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-ASM-002 · Update Maturity Declaration
`UC List!R110`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Self-Assessment
- **Portal:** Customer Portal
- **Description:** Update the customer's maturity declaration for a control, including status, owner and comments.
- **WBS Reference:** CP-17 Maturity self-declaration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-ASM-003 · View Self-Assessment Summary
`UC List!R111`

- **Actor:** Customer Admin, Customer User (+ assigned SGS roles, read-only)
- **Module/Feature:** Self-Assessment
- **Portal:** Customer Portal
- **Description:** View the distribution of maturity declarations across a framework or scope and the requirements still undeclared.
- **WBS Reference:** Implicit — CP-23 'Surface maturity self-declaration' (P1) — no dedicated self-assessment summary view
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User (xem), SGS Trainer/Assessor (xem), SGS Auditor/Certification (xem) — 'assigned SGS roles' hiểu là SGS User, Trainer/Assessor, Auditor/Certification [GIẢ ĐỊNH]
- *Phát hiện:* —

### 19. Readiness Indicators

`UC List!R112` · **ESt (Hour):** `=SUM(J113:J117)`

#### UC-RDN-001 · Calculate Readiness Indicators
`UC List!R113`

- **Actor:** System
- **Module/Feature:** Readiness Indicators
- **Portal:** System / Backend (No Portal)
- **Description:** Calculate evidence completeness and freshness and roll them up with maturity declarations, rule-based gaps and review states at the applicable scope/framework level.
- **WBS Reference:** CP-23 View readiness indicators (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-RDN-002 · Evaluate Rule-Based Gap Indicators
`UC List!R114`

- **Actor:** System
- **Module/Feature:** Readiness Indicators
- **Portal:** System / Backend (No Portal)
- **Description:** Apply deterministic MVP gap rules such as implemented without evidence, outdated evidence and missing maturity declaration, and explain each flag.
- **WBS Reference:** CP-18 Rule-based gap indicators (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-RDN-003 · Detect Outdated Evidence
`UC List!R115`

- **Actor:** System
- **Module/Feature:** Readiness Indicators
- **Portal:** System / Backend (No Portal)
- **Description:** Flag evidence as outdated when its expiry or review date drives a freshness issue and surface the result in readiness indicators.
- **WBS Reference:** CP-16 Upload evidence to control (P1); CP-23 View readiness indicators (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-RDN-004 · View Readiness Indicators
`UC List!R116`

- **Actor:** Customer Admin, Customer User, Customer Viewer (+ assigned SGS roles including SGS Consultant, read-only)
- **Module/Feature:** Readiness Indicators
- **Portal:** Customer Portal & SGS Portal
- **Description:** View a centralized readiness overview within Evidence Management for the selected scope/framework, including completeness, freshness, declared maturity, gap and review indicators, with drill-down to contributing requirements and evidence.
- **WBS Reference:** CP-23 View readiness indicators (P1); Q&A #23 — client confirmed centralized readiness overview integrated in Evidence Management
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS User (xem), SGS Trainer/Assessor (xem), SGS Auditor/Certification (xem), SGS Consultant (xem) — 'assigned SGS roles' hiểu là SGS User, Trainer/Assessor, Auditor/Certification, Consultant [GIẢ ĐỊNH]
- *Phát hiện:* F-15

#### UC-RDN-005 · View Gap List
`UC List!R117`

- **Actor:** Customer Admin, Customer User, SGS Consultant (assigned, read-only)
- **Module/Feature:** Readiness Indicators
- **Portal:** Customer Portal & SGS Portal
- **Description:** View the open rule-based gaps for a scope or framework with the explanation of the triggering condition. Assigned SGS Consultants may use this view to support Gap Analysis without creating separate structured gap-status or action-item records.
- **WBS Reference:** CP-18 Rule-based gap indicators (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS Consultant (xem)
- *Phát hiện:* —

### 20. Training & SGS Academy

`UC List!R118` · **ESt (Hour):** `=SUM(J119:J125)`

#### UC-TRN-001 · Browse SGS Academy Course Catalogue
`UC List!R119`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** SGS Academy
- **Portal:** Customer Portal
- **Description:** Browse the Academy catalogue retrieved from the Academy API, with a graceful message where the catalogue is unavailable.
- **WBS Reference:** CP-29 Course catalogue integration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 20
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-39

#### UC-TRN-002 · View Course Details
`UC List!R120`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** SGS Academy
- **Portal:** Customer Portal
- **Description:** View the course information returned by SGS Academy for a selected catalogue item.
- **WBS Reference:** CP-29 Course catalogue integration (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-39

#### UC-TRN-004 · Proceed to SGS Academy for Enrolment
`UC List!R121`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** SGS Academy
- **Portal:** Customer Portal
- **Description:** Hand off to SGS Academy for enrolment, cart and payment, which remain owned by Academy.
- **WBS Reference:** CP-31 Redirect to Academy for enrolment (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-TRN-005 · Retrieve Training Badges from Academy
`UC List!R122`

- **Actor:** System
- **Module/Feature:** SGS Academy
- **Portal:** System / Backend (No Portal)
- **Description:** Retrieve completed-course badge information from the Academy API and associate each badge with the corresponding user profile.
- **WBS Reference:** CP-32 Training badges display (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-TRN-006 · View Training Badges
`UC List!R123`

- **Actor:** rket
- **Module/Feature:** SGS Academy
- **Portal:** Customer Portal
- **Description:** View completed-course training badges on the dedicated badges/profile view, clearly distinguished from certifications.
- **WBS Reference:** CP-32 Training badges display (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Cờ dữ liệu:* Actor hiếm gặp (1 lần trong file): 'rket' — soát chính tả/tên vai trò
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* —
- *Phát hiện:* F-06

#### UC-TRN-008 · Link Badge to User Profile
`UC List!R124`

- **Actor:** Customer Admin
- **Module/Feature:** SGS Academy
- **Portal:** Customer Portal
- **Description:** Allow badges to be linked to the user profile and, where appropriate, to the customer organization training/capability view.
- **WBS Reference:** Explicit — CP-32 'Profile badges page' (P1) — organization capability view not named
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-TRN-009 · Browse On-site Training Catalogue
`UC List!R125`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Training & SGS Academy
- **Portal:** Customer Portal
- **Description:** View the catalogue of available on-site training services in DTP. DTP only displays/tracks on-site training for MVP and does not manage the actual training delivery.
- **WBS Reference:** —
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 14
- *Cờ dữ liệu:* ID có khoảng trắng thừa
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-08, F-25

### 21. Service Request

`UC List!R126` · **ESt (Hour):** `=SUM(J127:J136)`

#### UC-SRQ-001 · Submit Service Request
`UC List!R127`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Service Request
- **Portal:** Customer Portal
- **Description:** Submit a service request for an existing WBS-supported category, linked to the relevant scope/framework/certification. When launched from Evidence Management, pre-fill the scope, framework and evidence context. A Service Request may also be initiated from a Marketplace Consultant profile, in which case the customer-selected Consultant is carried into the Service Request.
- **WBS Reference:** CP-34 Submit service request (P1); A4 Service request trigger from Evidence Management (P1); Q&A #33 category detail still to confirm
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 18
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-30, F-34, F-36

#### UC-SRQ-002 · View Service Request List
`UC List!R128`

- **Actor:** Customer Admin, Customer User, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- **Module/Feature:** Service Request
- **Portal:** Customer Portal & SGS Portal
- **Description:** View service requests within the permitted boundary: own organization for customers, assigned customers for SGS users, assigned activities for auditors, and consulting-related requests for the SGS Consultant's assigned customer.
- **WBS Reference:** CP-36 Service request listing (P1); OPS-18 Service request operations (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- *Phát hiện:* —

#### UC-SRQ-003 · View Service Request Details
`UC List!R129`

- **Actor:** Customer Admin, Customer User, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- **Module/Feature:** Service Request
- **Portal:** Customer Portal & SGS Portal
- **Description:** View a request's full content, linked scope and evidence, status history and customer-visible correspondence within the permitted boundary. SGS Consultants are limited to consulting-related requests for their assigned customer.
- **WBS Reference:** CP-35 Service request status flow & notification (P1); Q&A #59f/#59g
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant
- *Phát hiện:* —

#### UC-SRQ-004 · Cancel Service Request
`UC List!R130`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Service Request
- **Portal:** Customer Portal
- **Description:** Withdraw a submitted request that is no longer required, before SGS delivery begins.
- **WBS Reference:** PRESALE WBS GAP — Customer cancellation/withdrawal is not priced and is absent from the CP-35 status set (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 4
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-30

#### UC-SRQ-005 · Triage Service Request
`UC List!R131`

- **Actor:** SGS User
- **Module/Feature:** Service Request
- **Portal:** SGS Portal
- **Description:** Assess a submitted request and accept or reject it with a reason.
- **WBS Reference:** OPS-18 Service request operations (P1); CP-35 Service request status flow & notification (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User
- *Phát hiện:* —

#### UC-SRQ-006 · Assign Service Request
`UC List!R132`

- **Actor:** SGS Admin, SGS User
- **Module/Feature:** Service Request
- **Portal:** SGS Portal
- **Description:** Assign or confirm the responsible SGS personnel for a Service Request based on the service type. For consulting requests, SGS may assign/confirm a Consultant, taking into account a customer-selected Consultant where applicable. For audit-related requests, SGS may assign the appropriate Auditor/Certification personnel.
- **WBS Reference:** OPS-18 Service request operations (P1); Q&A #34 manual assignment; Q&A #56 automated COI enforcement removed from MVP; Q&A #59f Consultant assignment by SGS
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin, SGS User
- *Phát hiện:* F-30, F-34, F-36

#### UC-SRQ-007 · Update Service Request Status
`UC List!R133`

- **Actor:** SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Service Request
- **Portal:** SGS Portal
- **Description:** Advance a request through its lifecycle to in progress or closed, triggering customer notification.
- **WBS Reference:** OPS-18 Service request operations (P1); CP-35 Service request status flow & notification (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-30

#### UC-SRQ-008 · Add Internal Comment to Service Request
`UC List!R134`

- **Actor:** SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Service Request
- **Portal:** SGS Portal
- **Description:** Record internal SGS notes that are not visible to the customer.
- **WBS Reference:** OPS-18 Service request operations (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-30

#### UC-SRQ-009 · Request Information from Customer
`UC List!R135`

- **Actor:** SGS User, SGS Trainer/Assessor
- **Module/Feature:** Service Request
- **Portal:** SGS Portal
- **Description:** Ask the customer for further information on a request and set it to information requested.
- **WBS Reference:** CP-35 Service request status flow & notification (P1); OPS-18 Service request operations (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User, SGS Trainer/Assessor
- *Phát hiện:* F-30

#### UC-SRQ-010 · Respond to Information Request
`UC List!R136`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Service Request
- **Portal:** Customer Portal
- **Description:** Provide the requested information so the request can proceed.
- **WBS Reference:** PRESALE WBS GAP — No customer reply channel on a service request is priced; CP-25 (P1) is the review response, a different object
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

### 22. Review Workflow

`UC List!R137` · **ESt (Hour):** `=SUM(J138:J151)`

#### UC-REV-001 · Create Review
`UC List!R138`

- **Actor:** SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Create a review for the relevant customer, scope, framework, service request and evidence context. MVP supports exactly two review types — Readiness Assessment Review and Audit Review — and both are initiated by SGS; customers do not initiate reviews.
- **WBS Reference:** OPS-12 Create review (P1); A2 review-context separation (P1); Q&A #24/#25
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-28, F-36

#### UC-REV-002 · Assign Reviewer to Review
`UC List!R139`

- **Actor:** SGS Admin, SGS User
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Assign the SGS person who will conduct the review.
- **WBS Reference:** PRESALE WBS GAP — Reviewer assignment is not priced; OPS-12 (P1) has no assignment bullet, CP-27 (P2) only displays assignment
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 5
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin, SGS User
- *Phát hiện:* —

#### UC-REV-003 · View Review Queue
`UC List!R140`

- **Actor:** SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** View assigned reviews with open items, items pending customer action and closed items.
- **WBS Reference:** CP-27 Review list & queues (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* —

#### UC-REV-004 · View Review Details
`UC List!R141`

- **Actor:** SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, Customer Admin, Customer User
- **Module/Feature:** Review Workflow
- **Portal:** Customer Portal & SGS Portal
- **Description:** View review context, scope/framework, relevant evidence, comments, requests, requirement/control-level review statuses and the derived overall Review status, filtered to what each role is permitted to see.
- **WBS Reference:** OPS-13 SGS review evidence and controls (P1); CP-25 Customer review response (P1); Q&A #26 meeting confirmation
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-36

#### UC-REV-005 · Update Requirement / Control Review Status
`UC List!R142`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Manually update the review status of each applicable Requirement/Criteria or Control within a Review. Different review items within the same Review may have different statuses at the same time.
- **WBS Reference:** CP-26 Review status per control (P1); Q&A #26 — client confirmed item-level status is manually updated by SGS
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-28

#### UC-REV-006 · Add Review Comment
`UC List!R143`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Comment at evidence level or requirement level within the review thread.
- **WBS Reference:** OPS-13 SGS review evidence and controls (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* —

#### UC-REV-007 · Request Clarification or Additional Evidence
`UC List!R144`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Raise a request to the customer for clarification or further evidence and set the item to await a response.
- **WBS Reference:** OPS-13 SGS review evidence and controls (P1); CP-26 Review status per control (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* —

#### UC-REV-008 · Raise Finding
`UC List!R145`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Record a finding against a requirement, with its classification and the response required.
- **WBS Reference:** PRESALE WBS GAP — No finding object is priced; CP-25 (P1) prices the customer's response to findings that nothing creates
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 16
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-28

#### UC-REV-011 · View Review Feedback
`UC List!R146`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Review Workflow
- **Portal:** Customer Portal
- **Description:** View SGS comments, clarification requests and findings for the user's assigned scope, labelled with the review context.
- **WBS Reference:** CP-25 Customer review response (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-31

#### UC-REV-012 · Respond to Review Request
`UC List!R147`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Review Workflow
- **Portal:** Customer Portal
- **Description:** Respond to a comment or clarification request and attach or revise evidence.
- **WBS Reference:** CP-25 Customer review response (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-REV-013 · Submit Corrective Action
`UC List!R148`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Review Workflow
- **Portal:** Customer Portal
- **Description:** Submit a corrective action against a finding, with the action taken and its evidence.
- **WBS Reference:** CP-25 Customer review response (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-REV-014 · Evaluate Customer Response
`UC List!R149`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Evaluate a customer's clarification, revised evidence or corrective-action response and update the review item/status accordingly.
- **WBS Reference:** OPS-13 SGS review evidence and controls (P1); CP-26 Review status per control (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* —

#### UC-REV-015 · Close Review
`UC List!R150`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Portal:** SGS Portal
- **Description:** Formally close a Review after all applicable Requirements/Criteria and Controls have been completed. Final closure is performed manually by an authorized SGS reviewer after the system-derived overall status indicates the review is ready for closure.
- **WBS Reference:** CP-26 Review status per control (P1); Q&A #26 — client confirmed manual item-level status, automatic overall roll-up and manual final Review closure by SGS
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 6
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* F-28

#### UC-REV-016 · Derive Overall Review Status
`UC List!R151`

- **Actor:** System
- **Module/Feature:** Review Workflow
- **Portal:** System / Backend (No Portal)
- **Description:** Automatically derive and update the overall Review status from the statuses of the applicable Requirements/Criteria and Controls within the Review. The derived status supports progress visibility and determines when the Review is eligible for final manual closure.
- **WBS Reference:** CP-26 Review status per control (P1); Q&A #26 — client confirmed automatic overall Review status roll-up
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-28

### 23. Certification Record Management

`UC List!R152` · **ESt (Hour):** `=SUM(J153:J155)`

#### UC-CRT-001 · Create Certification Record
`UC List!R153`

- **Actor:** SGS User
- **Module/Feature:** Certification Record
- **Portal:** SGS Portal
- **Description:** Manually create a certification record for an assigned customer and scope/framework using the configured certification fields.
- **WBS Reference:** OPS-21 SGS cert record administration (P1); Q&A #36 manual SGS creation for MVP
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User
- *Phát hiện:* F-16

#### UC-CRT-002 · Edit Certification Record
`UC List!R154`

- **Actor:** SGS User
- **Module/Feature:** Certification Record
- **Portal:** SGS Portal
- **Description:** Update permitted certification record fields, with every change captured in the audit trail.
- **WBS Reference:** OPS-21 SGS cert record administration (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User
- *Phát hiện:* F-16

#### UC-CRT-003 · View Certification Record List
`UC List!R155`

- **Actor:** Customer Admin, Customer User, Customer Viewer, SGS User, SGS Admin
- **Module/Feature:** Certification Record
- **Portal:** Customer Portal & SGS Portal
- **Description:** View certification records within the permitted boundary, with framework, scope, status and expiry.
- **WBS Reference:** CP-37 Certification listing (P1)
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User
- *Phát hiện:* F-16

### 25. Certification Maintenance

`UC List!R156` · **ESt (Hour):** `=SUM(J157:J163)`

#### UC-CMT-001 · Update Certification Lifecycle Status
`UC List!R157`

- **Actor:** SGS Admin, SGS User
- **Module/Feature:** Certification Maintenance
- **Portal:** SGS Portal
- **Description:** Update the certification lifecycle status using the MVP statuses defined in WBS, including active, surveillance, pending renewal, suspended, withdrawn and expired, with SGS-controlled transitions.
- **WBS Reference:** CP-39 Certification lifecycle statuses (P1); Q&A #38 confirms recurrence differs by standard (no additional recurrence feature added beyond current WBS)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin, SGS User
- *Phát hiện:* F-16

#### UC-CMT-002 · Generate Certification Milestone Notification
`UC List!R158`

- **Actor:** System
- **Module/Feature:** Certification Maintenance
- **Portal:** System / Backend (No Portal)
- **Description:** Generate alerts for upcoming certification renewal or surveillance milestones and surface them through the MVP notification mechanism.
- **WBS Reference:** CP-42 Cert renewal/surveillance notifications (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** Suggest to be included in P1
- **ESt (Hour):** 5
- *Nhóm phạm vi:* C — LTS đề xuất P2, SGS muốn giữ P1, đã có giờ
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-04, F-12, F-38

#### UC-CMT-003 · Suspend Certification
`UC List!R159`

- **Actor:** SGS Auditor/Certification
- **Module/Feature:** Certification Maintenance
- **Portal:** SGS Portal
- **Description:** Suspend a certification, with reason and effective date, and reflect the suspension in internal and shared views.
- **WBS Reference:** Explicit — CP-39 'suspended' + 'Transitions by SGS' (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Auditor/Certification
- *Phát hiện:* F-16

#### UC-CMT-004 · Withdraw Certification
`UC List!R160`

- **Actor:** SGS Auditor/Certification
- **Module/Feature:** Certification Maintenance
- **Portal:** SGS Portal
- **Description:** Withdraw a certification permanently, with reason and effective date, and revoke any external sharing of it.
- **WBS Reference:** Explicit — CP-39 'withdrawn' + 'Transitions by SGS' (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Auditor/Certification
- *Phát hiện:* F-16

#### UC-CMT-005 · Expire Certification
`UC List!R161`

- **Actor:** System
- **Module/Feature:** Certification Maintenance
- **Portal:** System / Backend (No Portal)
- **Description:** Set a certification to expired when its validity period ends without renewal.
- **WBS Reference:** Explicit — CP-39 'expired' (P1) — automatic expiry job not named
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-16

#### UC-CMT-006 · Reinstate Certification
`UC List!R162`

- **Actor:** SGS Auditor/Certification
- **Module/Feature:** Certification Maintenance
- **Portal:** SGS Portal
- **Description:** Return a suspended or expired certification to active status with the basis recorded.
- **WBS Reference:** Implicit — CP-39 'Transitions by SGS' (P1) — reinstatement is not among the named transitions
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Auditor/Certification
- *Phát hiện:* F-16

#### UC-CMT-007 · Generate Certification Milestone Notification
`UC List!R163`

- **Actor:** System
- **Module/Feature:** Certification Maintenance
- **Portal:** System / Backend (No Portal)
- **Description:** Notify the customer and the assigned SGS user of approaching expiry, renewal and surveillance milestones, per the scheme's configured offsets.
- **WBS Reference:** Explicit — CP-42 Cert renewal/surveillance notifications — 'Scheduled jobs' (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** Suggest to be included in P1
- **ESt (Hour):** 5
- *Nhóm phạm vi:* C — LTS đề xuất P2, SGS muốn giữ P1, đã có giờ
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* F-04, F-12, F-16, F-38

### 26. Digital Trust Passport & External Sharing

`UC List!R164` · **ESt (Hour):** `=SUM(J165:J170)`

#### UC-PSP-001 · View Digital Trust Passport
`UC List!R165`

- **Actor:** Customer Admin, Customer User, Customer Viewer
- **Module/Feature:** Digital Trust Passport
- **Portal:** Customer Portal
- **Description:** View the customer's Digital Trust Passport / trust view showing certification information and other approved current trust information supported by the Phase 1 WBS.
- **WBS Reference:** CP-37 Certification listing (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer
- *Phát hiện:* —

#### UC-PSP-002 · Configure Certification Visibility
`UC List!R166`

- **Actor:** Customer Admin
- **Module/Feature:** Digital Trust Passport
- **Portal:** Customer Portal
- **Description:** Decide which certifications are visible internally and which may be shared externally.
- **WBS Reference:** CP-40 Internal/external visibility controls (P1); Q&A #39 detail still to confirm
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-PSP-003 · Select Trust Information for Sharing
`UC List!R167`

- **Actor:** Customer Admin
- **Module/Feature:** Digital Trust Passport
- **Portal:** Customer Portal
- **Description:** Select which supported trust information is visible internally or externally, according to the configured visibility controls.
- **WBS Reference:** CP-40 Internal/external visibility controls (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-PSP-004 · Generate Shareable Trust Profile Link
`UC List!R168`

- **Actor:** Customer Admin
- **Module/Feature:** Digital Trust Passport
- **Portal:** Customer Portal
- **Description:** Generate a tokenized, read-only trust-profile link for external stakeholders, with expiry/revocation supported by the WBS. DTP login is not required for the recipient.
- **WBS Reference:** CP-41 Shareable trust profile link (P1); Q&A #40/#41
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-PSP-005 · View Shared Trust Profile
`UC List!R169`

- **Actor:** External Stakeholder
- **Module/Feature:** Digital Trust Passport
- **Portal:** External Shared View (No Portal)
- **Description:** View approved certification and trust information through a valid external share link without a DTP login, subject to link validity and the configured sharing controls.
- **WBS Reference:** CP-41 Shareable trust profile link (P1); Q&A #40
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* External Stakeholder
- *Phát hiện:* —

#### UC-PSP-007 · View Trust Profile Access Log
`UC List!R170`

- **Actor:** Customer Admin
- **Module/Feature:** Digital Trust Passport
- **Portal:** Customer Portal
- **Description:** View when and by whom a shared trust profile was accessed.
- **WBS Reference:** PRESALE WBS GAP — No customer-facing share access log is priced; CP-47 (P1) logs sharing actions for SGS Admin only
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

### 27. Operations Monitoring & Reporting

`UC List!R171` · **ESt (Hour):** `=SUM(J172:J174)`

#### UC-OPS-001 · View SGS Operations Dashboard
`UC List!R172`

- **Actor:** SGS Admin, SGS User
- **Module/Feature:** Operations Monitoring
- **Portal:** SGS Portal
- **Description:** View operational metrics within the affiliate and assignment boundary: active customers, open service requests, pending reviews, upcoming certification milestones, with drill-down to the underlying queues.
- **WBS Reference:** OPS-06 Admin overview dashboard (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** Suggest to be included in P1
- **ESt (Hour):** 22
- *Nhóm phạm vi:* C — LTS đề xuất P2, SGS muốn giữ P1, đã có giờ
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin, SGS User
- *Phát hiện:* F-12

#### UC-OPS-002 · Monitor Assigned Customer Journeys
`UC List!R173`

- **Actor:** SGS User
- **Module/Feature:** Operations Monitoring
- **Portal:** SGS Portal
- **Description:** Monitor journey stage and readiness progress across assigned customers to identify where SGS engagement is needed.
- **WBS Reference:** CP-09 Journey view (P1); OPS-06 Admin overview dashboard (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS User
- *Phát hiện:* —

#### UC-OPS-003 · Monitor Integration Health
`UC List!R174`

- **Actor:** SGS Admin
- **Module/Feature:** Operations Monitoring
- **Portal:** SGS Portal
- **Description:** Review integration failures and degraded-mode events exposed by the platform so operational intervention can be taken where required.
- **WBS Reference:** CP-50 Integration error handling (P1)
- **LTS suggestion:** Phase 2
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* B3 — LTS đề xuất P2, SGS chưa phản hồi
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 28. Consulting Services

`UC List!R175` · **ESt (Hour):** `=SUM(J176:J177)`

#### UC-CNS-001 · Add Consulting Comment
`UC List!R176`

- **Actor:** SGS Consultant
- **Module/Feature:** Consulting Services
- **Portal:** SGS Portal
- **Description:** Add customer-visible consulting comments within the assigned customer's requirement/control/evidence or gap context to support Implementation Support and Gap Analysis. MVP does not include structured recommendation/action-item tracking, consulting progress statuses or a system-generated final deliverable.
- **WBS Reference:** PRESALE WBS GAP — New customer-confirmed Consultant capability
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 14
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Consultant
- *Phát hiện:* F-18

#### UC-CNS-002 · View Consulting Comments
`UC List!R177`

- **Actor:** Customer Admin, Customer User, SGS Consultant
- **Module/Feature:** Consulting Services
- **Portal:** Customer Portal & SGS Portal
- **Description:** View consulting comments associated with the customer's compliance/evidence context. Customers may provide additional evidence through the existing Evidence Management flow, but MVP does not include chat or reply interaction on Consultant comments.
- **WBS Reference:** PRESALE WBS GAP — New customer-confirmed Consultant collaboration behavior
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS Consultant
- *Phát hiện:* —

### 29. DT Marketplace

`UC List!R178` · **ESt (Hour):** `=SUM(J179:J184)`

#### UC-MKT-001 · View DT Marketplace
`UC List!R179`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** DT Marketplace
- **Portal:** Customer Portal
- **Description:** View the DT Marketplace landing page and access the available Marketplace categories for MVP: Pentesting Services and Consultants.
- **WBS Reference:** NEW – Customer-confirmed Marketplace scope; Xavier confirmation 10-Sep-2026. Not included in presale WBS; add to task list for estimation.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-MKT-002 · View Pentesting Service List
`UC List!R180`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** DT Marketplace
- **Portal:** Customer Portal
- **Description:** View the list of available Pentesting Services provided in the Marketplace. MVP does not include search, filtering, booking or payment.
- **WBS Reference:** NEW – Customer-confirmed Marketplace scope; Pentesting list to be provided by SGS Taiwan team. Not included in presale WBS.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-40

#### UC-MKT-003 · View Pentesting Service Details
`UC List!R181`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** DT Marketplace
- **Portal:** Customer Portal
- **Description:** View details of a selected Pentesting Service. For third-party Pentesting Services, DTP only displays the supplied service/provider information such as website, email and phone; no in-platform booking or payment is required.
- **WBS Reference:** NEW – Customer-confirmed Marketplace scope; Xavier clarification on third-party Pentesting Services. Not included in presale WBS.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 8
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-36

#### UC-MKT-004 · View Consultant Details
`UC List!R182`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** DT Marketplace
- **Portal:** Customer Portal
- **Description:** View the list of Consultants available through the Marketplace. Each Consultant is represented as an individual profile rather than only as a generic consulting service. MVP does not include search or filtering.
- **WBS Reference:** NEW – Customer-confirmed Marketplace scope; Consultant list to be provided by SGS Taiwan team. Not included in presale WBS.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 10
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-05, F-34, F-40

#### UC-MKT-005 · Customer Admin, Customer User
`UC List!R183`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** DT Marketplace
- **Portal:** Customer Portal
- **Description:** View the profile and details of a selected Consultant. From the Consultant detail view, the customer can proceed to the existing Submit Service Request flow with that Consultant selected.
- **WBS Reference:** NEW – Customer-confirmed Marketplace scope; Xavier confirmed individual Consultant profiles and customer selection of a specific Consultant. Not included in presale WBS.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 12
- *Cờ dữ liệu:* Tên UC trùng nội dung cột Actor
- *Cờ dữ liệu:* Giá trị cột 'Use Case Name' giống giá trị thường gặp ở cột 'Actor' (có thể lệch cột)
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-05, F-34

#### UC-MKT-006 · Manage Marketplace Content
`UC List!R184`

- **Actor:** SGS Admin
- **Module/Feature:** DT Marketplace
- **Portal:** SGS Portal
- **Description:** Create, update, activate/deactivate and remove Marketplace content for Pentesting Services and Consultant profiles. Marketplace content is maintained by SGS Admin.
- **WBS Reference:** NEW – Customer-confirmed Marketplace administration; Xavier confirmed content is maintained by SGS Admin. Not included in presale WBS; requires estimation.
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** 28
- *Nhóm phạm vi:* A — có giờ, LTS không đề xuất lùi
- *Xử lý test:* Trong phạm vi test [GIẢ ĐỊNH – chờ Q-01]
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* F-34

### 30. Statement of Applicability

`UC List!R185` · **ESt (Hour):** `=SUM(J186:J191)`

#### UC-SOA-001 · Manage Statement of Applicability
`UC List!R186`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Statement of Applicability
- **Portal:** Customer Portal
- **Description:** Define and maintain whether each requirement/control is applicable or not applicable for a selected Scope and Framework, including the justification for exclusions.
- **WBS Reference:** —
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** —
- *Nhóm phạm vi:* E — không có đề xuất, không có giờ
- *Xử lý test:* Chưa xác định – chờ Q-15
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-02, F-14

#### UC-SOA-002 · View Statement of Applicability
`UC List!R187`

- **Actor:** Customer Admin, Customer User, SGS Admin, SGS Auditor, SGS Consultant (View Only)
- **Module/Feature:** Statement of Applicability
- **Portal:** Customer Portal & SGS Portal
- **Description:** View the Statement of Applicability for a selected Scope and Framework, including each requirement/control's applicability status and the justification for controls marked as not applicable.
- **WBS Reference:** —
- **LTS suggestion:** —
- **SGS Comments:** —
- **ESt (Hour):** —
- *Cờ dữ liệu:* Actor hiếm gặp (1 lần trong file): 'SGS Auditor' — soát chính tả/tên vai trò
- *Nhóm phạm vi:* E — không có đề xuất, không có giờ
- *Xử lý test:* Chưa xác định – chờ Q-15
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS Admin, SGS Auditor/Certification, SGS Consultant (xem) — 'SGS Auditor' hiểu là SGS Auditor/Certification [GIẢ ĐỊNH]
- *Phát hiện:* F-02, F-10, F-14

## Sheet: Future Release

### 1. Authentication

#### UC-AUTH-006 · Authenticate via Enterprise SSO
`Future Release!R3`

- **Actor:** All authenticated roles
- **Module/Feature:** Authentication
- **Description:** Authenticate through a customer or SGS enterprise identity provider, with roles derived from IdP claims.
- **WBS Reference:** Explicit — CP-02 Enterprise SSO readiness (P2 — adapter stub only)
- **Reason for Future Release:** Enterprise SSO is explicitly Phase 2 / readiness only, not part of the MVP user flow.
- **Portal:** Customer Portal & SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User, SGS Trainer/Assessor, SGS Auditor/Certification, SGS Consultant — tất cả 8 vai trò đăng nhập
- *Phát hiện:* —

### 7. Framework Content Management

#### UC-FWK-010 · Publish Framework Version
`Future Release!R5`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Description:** Publish a new version of a framework, making it available to new journeys while leaving in-flight journeys on their existing version.
- **WBS Reference:** Explicit — A8 'Version history retained' (P2)
- **Reason for Future Release:** Framework version publishing is Phase 2 (A8).
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-FWK-011 · Migrate Evidence Mappings to New Framework Version
`Future Release!R6`

- **Actor:** SGS Admin, System
- **Module/Feature:** Framework Content
- **Description:** Re-map existing customer evidence and maturity declarations onto a new framework version, reporting items that require manual re-mapping.
- **WBS Reference:** Explicit — A8 'Version migration and re-mapping of existing evidence' (P2)
- **Reason for Future Release:** Framework version migration and evidence re-mapping are Phase 2 (A8).
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin — System
- *Phát hiện:* —

### 9. Regulatory Discovery Configuration

#### UC-DCF-001 · View Question List
`Future Release!R8`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** View the discovery question bank with type, status and usage.
- **WBS Reference:** Implicit — OPS-07 'Configure Regulatory Discovery questions/logic (RD-14)' (P2) — one bullet covers the whole question bank
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14 mark the approach as low priority / to be decided.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-002 · View Question Details
`Future Release!R9`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** View a question's full configuration, including answer options and the rules that consume it.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-003 · Create Question and Answer Options
`Future Release!R10`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Create a discovery question with its answer options and input constraints.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-004 · Edit Question
`Future Release!R11`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Modify a question's wording, options or constraints.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-005 · Archive Question
`Future Release!R12`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Withdraw an obsolete question from future questionnaires while retaining historical responses.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-006 · View Questionnaire List
`Future Release!R13`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** View the configured discovery questionnaires with version and status.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2) — questionnaire as an object is not named
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-007 · View Questionnaire Details
`Future Release!R14`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** View a questionnaire's question composition, ordering and branching.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-008 · Create Discovery Questionnaire
`Future Release!R15`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Assemble questions into an ordered questionnaire for a defined discovery purpose.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-009 · Edit Discovery Questionnaire
`Future Release!R16`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Modify a questionnaire's composition, ordering or branching logic.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-010 · Archive Discovery Questionnaire
`Future Release!R17`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Withdraw an obsolete questionnaire while retaining completed discovery records.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery configuration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-011 · Import Applicability Rule Set
`Future Release!R18`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Import an SGS-supplied applicability rule file, with validation and an import result report.
- **WBS Reference:** Explicit — CP-11 'Import SGS rules content' (P1)
- **Reason for Future Release:** Applicability rule-set administration belongs to Regulatory Discovery, which Q&A #12–14 defer from the first pilot.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-012 · View Applicability Rule List
`Future Release!R19`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** View the rules that map answer combinations to recommended frameworks and obligation levels.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2) — rule set is not inspectable in any priced UI
- **Reason for Future Release:** Regulatory Discovery rule administration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-013 · Create or Edit Applicability Rule
`Future Release!R20`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Maintain an individual rule linking answer conditions to recommended frameworks, obligation level and next actions.
- **WBS Reference:** Implicit — OPS-07 RD questions/logic bullet (P2)
- **Reason for Future Release:** Regulatory Discovery rule administration is deferred from the first pilot; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-014 · Maintain Recommendation Explanation Text
`Future Release!R21`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Maintain the explanation shown to the customer for why a framework may apply, plus the mandatory indicative-only disclaimer.
- **WBS Reference:** Implicit — CP-11 'Explain each recommendation' (P1) renders it; authoring falls under OPS-07 (P2)
- **Reason for Future Release:** Recommendation content authoring belongs to deferred Regulatory Discovery configuration; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-DCF-015 · Configure Recommended Next Actions
`Future Release!R22`

- **Actor:** SGS Admin
- **Module/Feature:** Discovery Configuration
- **Description:** Configure which next actions a discovery outcome offers, such as start a readiness workspace, view training or submit a service request.
- **WBS Reference:** Implicit — CP-12 (P1) implements the runtime next steps; configuring them falls under OPS-07 (P2)
- **Reason for Future Release:** Discovery next-action configuration belongs to the deferred Regulatory Discovery approach; Q&A #12–14.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 16. Regulatory Discovery

#### UC-RGF-001 · View and Manage Regulatory Feed
`Future Release!R24`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Regulatory Discovery
- **Description:** Customer Portal
- **WBS Reference:** View applicable regulatory-feed items, filter them by sector, geography and date, and mark items as read.
- **Reason for Future Release:** Regulatory feed function in WBS (originally P2); Q&A #58 confirms inclusion in Phase 1
- **Portal:** —
- *Cờ dữ liệu:* Giá trị cột 'Description' giống giá trị thường gặp ở cột 'Portal' (có thể lệch cột)
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test [GIẢ ĐỊNH – chờ Q-02]
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* F-03

#### UC-DSC-001 · Complete and Submit Discovery Questionnaire
`Future Release!R25`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Regulatory Discovery
- **Description:** Start a discovery for an organization, product or system, answer the guided intake covering organization type, sector, geography, market and scope type, and submit it for evaluation. Saving and resuming a partial questionnaire is an alternate flow.
- **WBS Reference:** Explicit — CP-10 Guided intake questionnaire (P1), incl. 'Save draft'
- **Reason for Future Release:** Customer Regulatory Discovery intake is not part of the first pilot per Q&A #12–14; keep for a later release after the approach is agreed.
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-DSC-002 · Generate Applicability Result
`Future Release!R26`

- **Actor:** System
- **Module/Feature:** Regulatory Discovery
- **Description:** Evaluate submitted answers against the published rule set and produce recommended frameworks classified by obligation level, each with its explanation.
- **WBS Reference:** Explicit — CP-11 'Rules engine execution' (P1)
- **Reason for Future Release:** Applicability evaluation is deferred with Regulatory Discovery per Q&A #12–14.
- **Portal:** System / Backend (No Portal)
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-DSC-003 · View Discovery Result
`Future Release!R27`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Regulatory Discovery
- **Description:** Review the recommended frameworks, the rationale for each, the obligation level and the indicative-only disclaimer.
- **WBS Reference:** Explicit — CP-11 'display results to UI' + 'Explain each recommendation' (P1)
- **Reason for Future Release:** Discovery result presentation is deferred with Regulatory Discovery per Q&A #12–14.
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-DSC-004 · Create or Update Scope from Discovery Result
`Future Release!R28`

- **Actor:** Customer Admin
- **Module/Feature:** Regulatory Discovery
- **Description:** Create a new scope or update an existing one from the discovery outcome.
- **WBS Reference:** Explicit — CP-12 'create product/system/org scope' (P1)
- **Reason for Future Release:** Creating/updating scope from discovery is deferred with Regulatory Discovery per Q&A #12–14.
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-DSC-005 · Activate Recommended Frameworks
`Future Release!R29`

- **Actor:** Customer Admin
- **Module/Feature:** Regulatory Discovery
- **Description:** Select which recommended frameworks to activate on a scope.
- **WBS Reference:** Explicit — CP-12 Activate frameworks on journey (P1)
- **Reason for Future Release:** Activating recommended frameworks from discovery is deferred with Regulatory Discovery per Q&A #12–14.
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* F-26

### 17. Evidence Management

#### UC-EVD-009 · Bulk Upload Evidence
`Future Release!R31`

- **Actor:** Customer Admin
- **Module/Feature:** Evidence Management
- **Description:** Upload multiple evidence files and apply or edit metadata in bulk as an asynchronous job.
- **WBS Reference:** Explicit — CP-21 Bulk upload and bulk metadata edit (P2, Low priority)
- **Reason for Future Release:** Bulk evidence upload/edit is Phase 2 and low priority (CP-21).
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-EVD-017 · Create Evidence Package
`Future Release!R32`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** Evidence Management
- **Description:** Create and maintain a separate Evidence Package containing the evidence/documents to be submitted for a Readiness Assessment or Audit Review.
- **WBS Reference:** Explicit — CP-19 'Package builder UI' (P2)
- **Reason for Future Release:** Q&A #21 now confirms Evidence Package is a separate system object (Option A). Implementation remains Future Release because CP-19 places the package builder in Phase 2.
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-EVD-018 · Submit Evidence Package for Review
`Future Release!R33`

- **Actor:** Customer Admin
- **Module/Feature:** Evidence Management
- **Description:** Submit the separate Evidence Package to SGS for review, moving it into the submitted state and linking it to the applicable Review.
- **WBS Reference:** Explicit — CP-19 'Submit package status' + 'Link to Review Workflow' (P2); A4 evidence-to-service-request handoff (P1)
- **Reason for Future Release:** Q&A #21 confirms the separate Evidence Package concept; package submission remains Future Release because CP-19 is Phase 2.
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

### 19. Readiness Indicators

#### UC-RDN-006 · Create Readiness Snapshot
`Future Release!R35`

- **Actor:** System
- **Module/Feature:** Readiness Indicators
- **Description:** Persist a periodic readiness snapshot per scope and framework so that trends can be reported.
- **WBS Reference:** Explicit — A3 'Periodic readiness snapshots' (P2)
- **Reason for Future Release:** Periodic readiness snapshots are Phase 2 (A3).
- **Portal:** System / Backend (No Portal)
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-RDN-007 · View Readiness Trend
`Future Release!R36`

- **Actor:** Customer Admin, Customer User (+ assigned SGS roles, read-only)
- **Module/Feature:** Readiness Indicators
- **Description:** View improvement or deterioration in completeness and freshness over time for a scope and framework.
- **WBS Reference:** Explicit — A3 'Trend chart per scope and framework' + 'Surface on the Passport view' (P2)
- **Reason for Future Release:** Readiness trend visualization is Phase 2 (A3).
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User (xem), SGS Trainer/Assessor (xem), SGS Auditor/Certification (xem) — 'assigned SGS roles' hiểu là SGS User, Trainer/Assessor, Auditor/Certification [GIẢ ĐỊNH]
- *Phát hiện:* —

#### UC-RDN-008 · Export Readiness Report
`Future Release!R37`

- **Actor:** Customer Admin, Customer User, SGS User
- **Module/Feature:** Readiness Indicators
- **Description:** Export readiness and evidence status, with the preparation-metric disclaimer applied and subject to role and tenant permissions.
- **WBS Reference:** Explicit — CP-22 Export evidence/readiness report (P2); CP-24 Readiness reports (P2)
- **Reason for Future Release:** Readiness/evidence report export is Phase 2 (CP-22/CP-24).
- **Portal:** Customer Portal & SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, SGS User
- *Phát hiện:* —

### 20. Training & SGS Academy

#### UC-TRN-003 · View Recommended Training
`Future Release!R39`

- **Actor:** Customer Admin, Customer User
- **Module/Feature:** SGS Academy
- **Description:** View courses recommended for the scope's active frameworks and identified readiness gaps.
- **WBS Reference:** Explicit — CP-30 Framework-linked course recommendations (P2)
- **Reason for Future Release:** Framework-linked training recommendations are Phase 2 (CP-30).
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User
- *Phát hiện:* —

#### UC-TRN-007 · Approve Training Badge for Trust Profile
`Future Release!R40`

- **Actor:** Customer Admin
- **Module/Feature:** SGS Academy
- **Description:** Approve which badges may appear on the Digital Trust Passport and shared trust profile.
- **WBS Reference:** Explicit — CP-33 Optional badges on Passport (P2)
- **Reason for Future Release:** Selecting training badges for Passport display is Phase 2 (CP-33).
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

### 22. Review Workflow

#### UC-REV-009 · Accept Evidence Package
`Future Release!R42`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Description:** Accept a submitted evidence package as meeting the applicable review criteria.
- **WBS Reference:** Implicit — CP-20 'accepted' state (P2); CP-19 package submission (P2) — no explicit reviewer accept action
- **Reason for Future Release:** Evidence Package acceptance depends on the Phase 2 package workflow (CP-19/CP-20). Q&A #21 has clarified the package concept; timing remains Future Release.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* —

#### UC-REV-010 · Reject Evidence Package
`Future Release!R43`

- **Actor:** SGS Trainer/Assessor, SGS Auditor/Certification
- **Module/Feature:** Review Workflow
- **Description:** Reject a submitted package with reasons and the actions required from the customer.
- **WBS Reference:** Implicit — CP-20 'rejected' state (P2) — no explicit reviewer reject action
- **Reason for Future Release:** Evidence Package rejection depends on the Phase 2 package workflow (CP-20). Q&A #21 has clarified the package concept; timing remains Future Release.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Trainer/Assessor, SGS Auditor/Certification
- *Phát hiện:* —

### 23. Certification Record Management

#### UC-CRT-004 · View Certification Record Details
`Future Release!R45`

- **Actor:** Customer Admin, Customer User, Customer Viewer, SGS User, SGS Admin
- **Module/Feature:** Certification Record
- **Description:** View a record's full detail, attached certificate documents, surveillance and renewal milestones, and its history of previous certificates, renewals and status changes.
- **WBS Reference:** Explicit — CP-38 Certification details and history (P2)
- **Reason for Future Release:** Certification details/history is Phase 2 (CP-38).
- **Portal:** Customer Portal & SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin, Customer User, Customer Viewer, SGS Admin, SGS User
- *Phát hiện:* —

#### UC-CRT-005 · Upload Certificate Document
`Future Release!R46`

- **Actor:** SGS User
- **Module/Feature:** Certification Record
- **Description:** Attach the issued certificate document to a record in secure storage, marked as SGS-verified.
- **WBS Reference:** Explicit — A9 Upload certificate (P2); CP-49 secure document storage (P1)
- **Reason for Future Release:** Certificate document upload is Phase 2 capability (A9); secure storage alone being P1 does not make the business UC MVP.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS User
- *Phát hiện:* —

#### UC-CRT-006 · Register Customer-Provided Certification
`Future Release!R47`

- **Actor:** Customer Admin
- **Module/Feature:** Certification Record
- **Description:** Record a certification the organization holds from SGS or a third party outside DTP, stored as customer-provided information and visually distinguished from SGS-verified records.
- **WBS Reference:** Explicit — A9 Upload certificate — 'customer-uploaded cert documents' (P2)
- **Reason for Future Release:** Customer-provided certification registration is Phase 2 (A9).
- **Portal:** Customer Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* Customer Admin
- *Phát hiện:* —

#### UC-CRT-007 · Set Trust Information Provenance
`Future Release!R48`

- **Actor:** System, SGS User
- **Module/Feature:** Certification Record
- **Description:** Assign and carry the provenance of every trust record — SGS-verified, SGS assessment, customer-provided, third-party or automated signal — through display, sharing and export.
- **WBS Reference:** Explicit — A9 'Provenance attribute on trust records' + 'Provenance badge' + 'carried through export' (P2)
- **Reason for Future Release:** Trust-information provenance model/badging is Phase 2 (A9).
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS User — System
- *Phát hiện:* —

#### UC-CRT-008 · View Certification Reporting
`Future Release!R49`

- **Actor:** SGS Admin
- **Module/Feature:** Certification Record
- **Description:** Report on certification records by type, status, expiry, scope, geography and customer account.
- **WBS Reference:** Explicit — OPS-22 Cert reporting (P2, Low priority)
- **Reason for Future Release:** Certification reporting is Phase 2 / low priority (OPS-22).
- **Portal:** SGS Portal
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 26. Digital Trust Passport & External Sharing

#### UC-PSP-006 · Verify Shared Trust Information
`Future Release!R51`

- **Actor:** External Stakeholder
- **Module/Feature:** Digital Trust Passport
- **Description:** Verify the authenticity of shared certification and trust information through the platform's verification mechanism.
- **WBS Reference:** Explicit — CP-43 Share verification (advanced) (P2, Low priority)
- **Reason for Future Release:** Advanced share verification is Phase 2 / low priority (CP-43).
- **Portal:** External Shared View (No Portal)
- *Nhóm phạm vi:* Future Release (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* External Stakeholder
- *Phát hiện:* —

## Sheet: OOS - Not MVP

### 4. Impartiality & Conflict-of-Interest Control

#### UC-COI-001 · Evaluate Conflict of Interest on Assignment
`OOS - Not MVP!R3`

- **Actor:** System
- **Module/Feature:** Impartiality Control
- **Description:** Cross-check a proposed assignment of an SGS person to a customer scope against service requests, prior readiness reviews, assessment activity, audit activity, certification activity and evidence review history, then block or flag it per the configured rules.
- **WBS Reference:** Explicit — CP-48 'COI rule engine' (P1); OPS-09 'COI checks before grant' (P1); OPS-18 'enforce COI rules' (P1)
- **Reason for OOS / Not MVP:** Explicitly removed from the MVP by customer confirmation Q&A #56 ('Let's remove from MVP scope, not critical at this stage'). Q&A #47 also states COI is not really required for the MVP.
- **Portal:** System / Backend (No Portal)
- *Nhóm phạm vi:* OOS / Not MVP (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* System
- *Phát hiện:* —

#### UC-COI-002 · Override Conflict-of-Interest Warning
`OOS - Not MVP!R4`

- **Actor:** SGS Admin
- **Module/Feature:** Impartiality Control
- **Description:** Record a justified override of a flagged (non-blocking) conflict, capturing the reason and approver.
- **WBS Reference:** Explicit — CP-48 'Log checks/overrides' (P1)
- **Reason for OOS / Not MVP:** Explicitly removed from the MVP together with COI controls by customer confirmation Q&A #56.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* OOS / Not MVP (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-COI-003 · Configure Conflict-of-Interest Rules
`OOS - Not MVP!R5`

- **Actor:** SGS Admin
- **Module/Feature:** Impartiality Control
- **Description:** Maintain the rule set that determines which role and service combinations are incompatible on the same customer scope.
- **WBS Reference:** Implicit — CP-48 rule engine (P1) — no rule configuration UI priced; PRD NFR-MNT-03 says 'where feasible'
- **Reason for OOS / Not MVP:** Explicitly removed from the MVP together with COI controls by customer confirmation Q&A #56.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* OOS / Not MVP (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

#### UC-COI-004 · View Conflict-of-Interest Check History
`OOS - Not MVP!R6`

- **Actor:** SGS Admin
- **Module/Feature:** Impartiality Control
- **Description:** Review past conflict checks, warnings, overrides and assignment decisions for accreditation and internal audit purposes.
- **WBS Reference:** Implicit — CP-48 'Log checks/overrides' (P1) + CP-47 Audit Log UI (P1) — no dedicated COI history view
- **Reason for OOS / Not MVP:** Explicitly removed from the MVP together with COI controls by customer confirmation Q&A #56.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* OOS / Not MVP (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

### 7. Framework Content Management

#### UC-FWK-012 · Map Controls Across Frameworks
`OOS - Not MVP!R8`

- **Actor:** SGS Admin
- **Module/Feature:** Framework Content
- **Description:** Maintain equivalence mappings between controls of different frameworks so that shared evidence and shared controls can be recognised.
- **WBS Reference:** NOT DEFINED — Cross-framework control equivalence mapping is not priced anywhere
- **Reason for OOS / Not MVP:** Explicitly OUT OF MVP by customer confirmation Q&A #18: ISO 27001 / ISO 42001 requirement cross-mapping is excluded from the MVP.
- **Portal:** SGS Portal
- *Nhóm phạm vi:* OOS / Not MVP (theo sheet)
- *Xử lý test:* Ngoài phạm vi test (theo sheet)
- *Vai trò (chuẩn hóa):* SGS Admin
- *Phát hiện:* —

## Sheet: Pending Clarification

Dòng có dữ liệu nhưng không phải UC hay tiêu đề section (chép nguyên văn):

| Dòng | Nội dung |
|---|---|
| R2 | UC ID: No pending clarification use cases currently tracked |

_Không có UC._
