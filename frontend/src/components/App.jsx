import React, { useEffect ,useState} from 'react';
import { render } from 'react-dom';
import '../index.css';


const App = () => {
    const [information, setInformation] = useState([]);
    const fetchmovies=()=>{
        fetch('/api/getmovies')
        .then((data)=>data.json()).then((data)=>{
            setInformation(data.data)    
        })
            // setInformation([data.data]);
        }
    
    
    useEffect(() => {
        
            fetchmovies();
        
    }, [])
    return (

        <div className='h-[220px]' >
            <h1 className='bg-gray-700 text-white p-3 m-4 flex justify-center' >Shows liked by me</h1>
            
            <div className="flex flex-wrap justify-center">
                {information.map((movie, index) => (
                    <div key={index} className="bg-white rounded-lg shadow-lg p-4 m-4 w-80">
                        <img 
                            src={movie.img_url} 
                            alt={`${movie.name} poster`} 
                            className="w-full h-48 object-cover rounded-lg"
                        />
                        <h1 className="text-xl font-bold mt-2">{movie.name}</h1>
                        <p className="text-gray-700">{movie.desc}</p>
                        <p className="text-yellow-500 font-semibold">Rating: {movie.rating}</p>
                    </div>
                ))}
            </div>

        {console.log("Working2")}
       
        </div>
    )
}
export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv);