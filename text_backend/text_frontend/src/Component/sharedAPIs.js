import axios from "axios";

export function get_headers() {
  return axios
      .get("/api/headers/")
}