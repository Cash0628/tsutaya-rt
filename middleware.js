// middleware.js
import { NextResponse } from "next/server";

export function middleware(request) {
  const basicAuth = request.headers.get("authorization");

  const username = "RT2025"; // ← 這裡改成你要的帳號
  const password = "80290038"; // ← 這裡改成你要的密碼

  if (basicAuth) {
    const authValue = basicAuth.split(" ")[1];
    const [user, pass] = atob(authValue).split(":");

    if (user === username && pass === password) {
      return NextResponse.next();
    }
  }

  const headers = new Headers();
  headers.set("WWW-Authenticate", 'Basic realm="Enter username and password"');

  return new Response("Authentication required.", {
    status: 401,
    headers,
  });
}
