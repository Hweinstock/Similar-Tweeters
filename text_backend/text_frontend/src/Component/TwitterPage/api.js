import axios from "axios";

export function get_recent_tweets(username){
    let params = {
            params: {
                username: username,
            }
    };

    return axios.get('/api/twitter/recent', params)
}

export default { get_recent_tweets }
