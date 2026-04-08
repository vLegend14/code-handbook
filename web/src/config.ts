export const API_URL = import.meta.env.PUBLIC_API_URL ?? "http://localhost:3001";

export const WS_URL  = API_URL.replace(/^http/, "ws");
