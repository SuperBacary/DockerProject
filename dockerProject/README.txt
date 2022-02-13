#pour build l'image  
docker build -t python . 

#pour run le conteneur 
docker run -idt --name python -p 4242:5000 --mount source=monvolume,target=/data python


#pour creer le deployment et le service associé 
kubectl apply -f config.yaml  

#pour faire gerer les routes statiques du service
minikube tunnel