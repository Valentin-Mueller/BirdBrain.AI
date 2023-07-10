import Head from 'next/head';
import { useState } from 'react'; // Add this line
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
  }}
  // Add these lines
   const [selectedImage, setSelectedImage] = useState(null);
   const [imageUrl, setImageUrl] = useState(null);
   const [isImageLoaded, setIsImageLoaded] = useState(false);
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
    handleImageUpload(file);
  };

  const onImageLoad = () => {
    setLoading(true);
    setIsImageLoaded(true); // Set isImageLoaded to true when image has loaded

  };

  const handleImageUpload = async (file) => {
    const formData = new FormData();
    formData.append('file', file);

    // Now formData is defined, we need it in our fetch request
    await fetch('http://localhost:8000/api/photo', {
      method: 'POST',
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
      })
      .catch((error) => {
        console.error(error);
      });
  };


  return (
    <div className={styles.container}>
      <Head>
        <title>Create Next App</title>
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to BirdBrain.AI &#128039;
        </h1>

        <p className={styles.description}>
          Get started by choosing an bird image
        </p>


        <div>
      <div id='Image-placeholder'>
        {imageUrl && <img id="preview-image" src={imageUrl} alt="Preview" onLoad={onImageLoad}  />}
        <br/>
        <input
            type="file"
            accept="image/*"
            onChange={handleImageChangeAndUpload}
        />
      </div>
        </div>
       {isImageLoaded &&
    <div id='text-placeholder'>
        <p>Your text here</p>
    </div>
      }

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
