// Types matching our Django models
export interface User {
  id: number;
  username: string;
  email: string;
}

export interface Extension {
  id: number;
  name: string;
  slug: string;
  description: string;
  developer: User;
  icon: string | null;
  extension_file: string;
  status: "pending" | "approved" | "rejected" | "flagged";
  downloads: number;
  created_at: string;
  reviews?: Review[];
  flags?: ModerationFlag[];
}

export interface Review {
  id: number;
  extension: number;
  reviewer: User;
  decision: "approved" | "rejected" | "needs_changes";
  commments: string;
  created_at: string;
}

export interface ModerationFlag {
  id: number;
  extension: number;
  check_name: string;
  severtity: "info" | "warning" | "critical";
  message: string;
  created_at: string;

}
