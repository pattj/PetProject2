using Microsoft.AspNetCore.Mvc;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using PetProject2.Models;

namespace PetProject2.Controllers
{
    public class PetController : Controller
    {
        private IPetsRepository repository;

        public PetController (IPetsRepository repo)
        {
            repository = repo;
           
        }

        public ViewResult List() => View(repository.Pets);
    }
}
