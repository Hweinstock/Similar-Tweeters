import axios from "axios";

const comp = {
  id: 0,
  label: 'book'
};

export function submit_texts(texts) {

  let get_params = {
    params: {
      label: comp.label,
      texts: {
        text1: texts.left,
        text2: texts.right,
      },
    }
  };
  return axios
      .get("/api/compareRawText/", get_params)

}

export function get_headers() {
  return axios
      .get("/api/headers/")
}

export function get_text_objects(text) {
  let get_data = {
    params:
        {
          text: text,
          label: comp.label,
        },
  };
  return axios
      .get("/api/analyzeText/", get_data)
}

export default {submit_texts, get_headers, get_text_objects}