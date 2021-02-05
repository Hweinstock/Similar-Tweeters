import axios from "axios";

const comp = {
  id: 0,
  label: 'book'
};

export function make_comparison(id) {
  return axios
      .get("/api/comps/"+id)
}

export function submit_texts(texts) {

  let extended_comp = comp;
  extended_comp.text1 = texts.box1;
  extended_comp.text2 = texts.box2;

  return axios
      .post("/api/comps/", comp)

  // axios
  //     .post("/api/comps/", comp)
  //     .then(response => make_comparison(response.data.id)
  //         .then(response =>))
  //     .catch(error => error);
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

export default {submit_texts, get_headers, make_comparison, get_text_objects}