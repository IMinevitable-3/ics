import React, { useState } from "react";
import axios from "axios";
import { MapContainer, TileLayer, Marker, Popup } from "react-leaflet";

const FormWithMap = () => {
  const [formData, setFormData] = useState({
    lattitude: "",
    longitude: "",
    distance: "",
  });
  const [coordinates, setCoordinates] = useState([]);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      const response = await axios.post(
        "http://localhost:8000/api/get-grid",
        formData
      );
      setCoordinates(response.data);
    } catch (error) {
      console.error("Error fetching coordinates:", error);
    }
  };

  return (
    <>
      <div style={{ display: "flex" }}>
        <form onSubmit={handleSubmit}>
          <div style={{ display: "flex", flexDirection: "row", gap: "2rem" }}>
            <label>
              Latitude:
              <input
                type="text"
                name="lattitude"
                value={formData.lattitude}
                onChange={handleChange}
              />
            </label>
            <br />
            <label>
              Longitude:
              <input
                type="text"
                name="longitude"
                value={formData.longitude}
                onChange={handleChange}
              />
            </label>
            <br />
            <label>
              Distance:
              <input
                type="text"
                name="distance"
                value={formData.distance}
                onChange={handleChange}
              />
            </label>
          </div>
          <br />
          <button
            type="submit"
            style={{
              justifyContent: "center",
              alignItems: "center",
            }}
          >
            Submit
          </button>
        </form>
      </div>
      <MapContainer
        center={[37.7749, -122.4194]}
        zoom={1}
        style={{ height: "400px", width: "100%" }}
      >
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {coordinates.map((coordinateSet, index) => (
          <React.Fragment key={index}>
            {coordinateSet.map((coordinate, i) => (
              <Marker key={i} position={[coordinate[0], coordinate[1]]}>
                <Popup>{`Latitude: ${coordinate[0]}, Longitude: ${coordinate[1]}`}</Popup>
              </Marker>
            ))}
          </React.Fragment>
        ))}
      </MapContainer>
    </>
  );
};

export default FormWithMap;
