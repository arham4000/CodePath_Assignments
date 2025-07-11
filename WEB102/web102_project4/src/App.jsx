import { useState, useEffect } from 'react';
import './App.css';
const ACCESS_KEY = import.meta.env.VITE_APP_ACCESS_KEY;

function App() {

  const [currentImage, setCurrentImage] = useState(null)
  const [currentBreed, setCurrentBreed] = useState('')
  const [currentOrigin, setCurrentOrigin] = useState('')
  const [currentLifeSpan, setCurrentLifeSpan] = useState('')

  useEffect( () => {
    makeQuery();
  }, [])


  const makeQuery = () => {
    const query = `https://api.thecatapi.com/v1/images/search?limit=1&api_key=${ACCESS_KEY}&has_breeds=1`
    callAPI(query).catch(console.error)
  };

  const submitForm = () => {
    makeQuery();
  }

  const callAPI = async (query) => {
    const response = await fetch(query)
    const responseJSON = await response.json()
    setCurrentImage(responseJSON[0].url)
    setCurrentBreed(responseJSON[0].breeds[0].name)
    setCurrentOrigin(responseJSON[0].breeds[0].origin)
    setCurrentLifeSpan(responseJSON[0].breeds[0].life_span)

  }

  return (
    <div className='page-container'>
      <h1>Random Cat Image Generator</h1>

      <div className='image-container'>
        <h2>Request an Image!</h2>
        <img
          src={currentImage}
          alt="Random Cat Image"
          width='400px'
        />
        <div className='attribute-container'>
          <h3>Cattributes</h3>
          <p>Breed: {currentBreed}</p>
          <p>Origin: {currentOrigin}</p>
          <p>Life-Span: {currentLifeSpan}</p>
        </div>
        <br></br>
        <button onClick={submitForm}>
          Another One!
        </button>
      </div>

      <div className='banlist-container'>
        <p>ban list</p>
      </div>

    </div>
  )
}

export default App
