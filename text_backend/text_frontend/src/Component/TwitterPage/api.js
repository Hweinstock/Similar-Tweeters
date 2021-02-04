import axios from "axios";

export function get_recent_tweets(username){
    let params = {
            params: {
                username: username,
            }
    };

    return axios.get('/api/twitter/recent', params)
}


export function get_from_username(username){
    let get_data = {
        params: {
            username: username,
        },
    };

    return axios.get('/api/fromUsername/', get_data)
}

export function post_create_text(post_data){

    return axios.post('/api/text/', post_data)


}

export function get_text_analyzer(id){
    let get_data = {
        params: {
            id: id,
        }
    };

    return axios.get('/api/text/analyzeText/', get_data)
}



export default { get_recent_tweets, get_from_username, post_create_text, get_text_analyzer }
