import Head from 'next/head';
import { useState, useRef } from 'react'; // Add this line
import styles from '../styles/Home.module.css';

export default function Home() {
  const callAPI = async () => {
    try {
      const res = await fetch('http://localhost:8000/test');
      const data = await res.json();
      alert(JSON.stringify(data));
    } catch (err) {
      alert(JSON.stringify(err));
      // {(event) => ImageUpload(event)}
    }
  };

  const fileInputRef = useRef(null);

  // Add these lines
  const [selectedImage, setSelectedImage] = useState(null);
  const [imageUrl, setImageUrl] = useState(null);
  const [isImageLoaded, setIsImageLoaded] = useState(false);
  const [loading, setLoading] = useState(false);

  const [birdName, setBirdName] = useState('');
  const [confidence, setConfidence] = useState(0);
  const [detailed, setDetailed] = useState(false);
  const [birdInfo, setBirdInfo] = useState(null);

  const handleImageChangeAndUpload = (event) => {
    const file = event.target.files[0];
    setSelectedImage(file);

    // Preview the selected image
    const reader = new FileReader();
    reader.onloadend = () => {
      setImageUrl(reader.result);
    };
    reader.readAsDataURL(file);

    // Trigger the image upload
    handleBirdClassification(file);
  };

  const handleCustomButtonClick = () => {
    fileInputRef.current.click();
  };

  const onImageLoad = () => {
    setLoading(true);
    setIsImageLoaded(true); // Set isImageLoaded to true when image has loaded
  };

  const handleBirdClassification = async (file) => {
    const formData = new FormData();
    formData.append('image', file);

    const response = await fetch('http://localhost:8000/classify-bird', {
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json();
      console.error('Server Error:', errorData);
      // Handle the error condition here, such as showing an error message to the user.
      return;
    }

    const data = await response.json();
    console.log('Server Response:', data);

    // Update the state with the received data
    setBirdName(data.bird_name);
    setConfidence(data.confidence);
  };

  const fetchBirdInformation = async () => {
    const formData = new FormData();
    formData.append('bird_name', birdName);
    formData.append('detailed', detailed);

    const response = await fetch('http://localhost:8000/bird-information', {
      // headers: {
      //   'Content-Type': 'application/json',
      // },
      method: 'POST',
      body: formData,
    });

    if (!response.ok) {
      const errorData = await response.json();
      throw new Error(errorData.detail);
    }

    const data = await response.json();
    setBirdInfo(data.bird_information);
  };

  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>Welcome to BirdBrain.AI &#128039;</h1>

        <p className={styles.description}>Get started by choosing an bird image</p>

        <div>
          <div id="Image-placeholder">
            {imageUrl && (
              <img
                id="preview-image"
                src={imageUrl}
                alt="Preview"
                onLoad={onImageLoad}
                className={styles.previewImage}
              />
            )}
          </div>
          <div className={styles.buttonContainer}>
            <input
              type="file"
              accept="image/*"
              id="fileInput"
              ref={fileInputRef}
              onChange={handleImageChangeAndUpload}
              hidden
            />
            <label htmlFor="fileInput" className={styles.uploadButton} onClick={handleCustomButtonClick}>
              Choose an Image
            </label>
          </div>
        </div>
        {birdName && (
          <div className={styles.birdInfo}>
            <div>
              <h3>{birdName}</h3>
              <p className={styles.confidence}>Confidence: {(confidence * 100).toFixed(2) + '%'}</p>
            </div>
            <button onClick={fetchBirdInformation} className={styles.uploadButton}>
              More Information
            </button>
            <label>
              <input type="checkbox" checked={detailed} onChange={(e) => setDetailed(e.target.checked)} />
              Detailed
            </label>
            {birdInfo && (
              <div>
                <p>{birdInfo}</p>
              </div>
            )}
          </div>
        )}
      </main>

      <footer className={styles.footer}>
        <a
          href="https://vercel.com?utm_source=create-next-app&utm_medium=default-template&utm_campaign=create-next-app"
          target="_blank"
          rel="noopener noreferrer"
        >
          Powered by <img src="/vercel.svg" alt="Vercel Logo" className={styles.logo} />
        </a>
      </footer>
    </div>
  );
}
