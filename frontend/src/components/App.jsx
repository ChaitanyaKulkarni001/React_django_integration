import React from 'react';
import { render } from 'react-dom';
import '../index.css';
const App = () => {
    return (

        <div className='h-[220px]' >
            <h1 className='bg-black text-white' >Hello this k,nj is william</h1>


        <h3 className='flex justify-center items-center bottom-0 bg-fuchsia-900 text-white rounded-full' >
            ABhiajana mandastimira mihir sokhya nagari
        </h3>
        </div>
    )
}
export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);