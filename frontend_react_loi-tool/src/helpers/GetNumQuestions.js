// System imports
//import React from 'react'

// Local imports
import getProxyRoute from './ProxyRoute'

// // // Question Generation
// async version
/*async function get_num_questions(endpoint) {
    console.log('requesting question from /api/num_questions')
    //const response = await axios.get(proxy_route+'/api/question');
    const response = await fetch(proxy_route + '/api/num_questions', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({ endpoint })
        }
    );
    //console.log(response);
    const data = await response.json();
    //console.log(data);
    return data.n_questions;
}*/

// non-async
function get_num_questions(endpoint) {
    const proxy_route = getProxyRoute();
    console.log('requesting question from /api/num_questions')
    return fetch(proxy_route + '/api/num_questions', {
            method:'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body:JSON.stringify({ endpoint })
        }
    )
    .then(response=>response.json());
}


async function getNumQs(endpoint_val){
    //return get_num_questions(endpoint_val);
    //const bob = QABlock({question_ndx: 0, endpoint_val: });
    // instatiate question block for each one
    /*const bob = [];
    console.log('testing1: '+n_questions)
    for (let i = 0; i < n_questions; i++){
        const elem = <QABlock question_ndx={i} endpoint_val={endpoint_val} />;
        //ReactDOM.render(elem, document.getElementById('root'));
        //qaBlocks.push(elem);
        //console.log(<QABlock question_ndx={i} endpoint_val={endpoint_val} />);
        //qaBlocks.push(<div key={i}>{QABlock({question_ndx: 0, endpoint_val: endpoint_val})}</div>);
        qaBlocks.push(<div key={i}>{elem}</div>);
    }
    console.log('testing2 len:'+qaBlocks.length)

    return (qaBlocks);*/
    return;
}