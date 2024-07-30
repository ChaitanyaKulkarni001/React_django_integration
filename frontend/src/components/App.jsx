import React from 'react';
import { render } from 'react-dom';
import '../index.css';
const App = () => {
    return (

        <div className='h-[220px]' >
            <h1 className='bg-gray-700 text-white' >Hello, William Butcher this side</h1>
            


       
        </div>
    )
}
export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);